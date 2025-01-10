"""Ten-Item Personality Inventory (TIPI)"""
import velesresearch as vls
from velesresearch.models import PageModel

def tipi(
    name: str = "TIPI",
    instruction: str | None = None,
    questionOptions: dict | None = None,
    pageOptions: dict | None = None,
) -> PageModel:
    """
    ## Ten-Item Personality Inventory (TIPI)
        10-item measure of the Big-Five dimensions is offered for situations where very short measures are needed, personality is not the primary topic of interest, or researchers can tolerate the somewhat diminished psychometric properties associated with very brief measures.
    
    ## Original
        <div class="csl-bib-body" style="line-height: 2; margin-left: 2em; text-indent:-2em;">
        <div class="csl-entry">Gosling, S. D., Rentfrow, P. J., &amp; Swann, W. B. (2003). A very brief measure of the Big-Five personality domains. <i>Journal of Research in Personality</i>, <i>37</i>(6), 504–528. <https://doi.org/10.1016/S0092-6566(03)00046-1></div>
        </div>
    
    ## Score calculation
        An average.

    ## Reverse items
        2, 4, 6, 8, 10
    
    ## Subscales
        1. Extraversion: 1, 6
        2. Agreeableness: 2, 7
        3. Conscientiousness: 3, 8
        4.  Emotional Stability: 4, 9
        5.  Openness to Experiences: 5, 10

    ## Reliability
        1. Extraversion: α = .68
        2. Agreeableness: α = .4
        3. Conscientiousness: α = .5
        4.  Emotional Stability: α = .73
        5.  Openness to Experiences: α = .45

    ## Implemented by
        Julia Jankowska (University of Wrocław)

    Args:
        name (str): Base name for pages and questions. Defaults to "TIPI".
        instruction (str): Instruction for the questionnaire. None means that the default instruction will be used.
        questionOptions (dict | None): Additional options for questions as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the TIPI questionnaire. Use the `*` operator to unpack it to questions.
    """
    if instruction is None:
        instruction = """Here are a number of personality traits that may or may not apply to you. Please write a number next to each statement to indicate the extent to which you agree or disagree with that statement. You should rate the extent to which the pair of traits applies to you, even if one characteristic applies more strongly than the other.

<b>I see myself as:</b>"""

    if questionOptions is None:
        questionOptions = {}

    if pageOptions is None:
        pageOptions = {}

    items = """Extraverted, enthusiastic.
Critical, quarrelsome.
Dependable, self-disciplined.
Anxious, easily upset.
Open to new experiences, complex.
Reserved, quiet.
Sympathetic, warm.
Disorganized, careless.
Calm, emotionally stable.
Conventional, uncreative.""".split(
        "\n"
    )

    scale = """1 – Disagree strongly
2 – Disagree moderately
3 – Disagree a little
4 – Neither agree nor disagree
5 – Agree a little
6 – Agree moderately
7 – Agree strongly""".split(
  "\n"
    )

    return vls.page(
        name + "_page",
        vls.info(name + "_instruction", instruction),
        vls.radio(
            name,
            items,
            scale,
            **questionOptions,
        ),
        **pageOptions,
    )
