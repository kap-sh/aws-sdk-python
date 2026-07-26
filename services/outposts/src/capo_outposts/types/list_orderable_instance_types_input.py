"""Generated from Smithy shape ``com.amazonaws.outposts#ListOrderableInstanceTypesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.max_results1000
    import capo_outposts.types.outpost_generation
    import capo_outposts.types.token


class ListOrderableInstanceTypesInput(TypedDict, closed=True):
    outpost_generation_filter: NotRequired[
        "capo_outposts.types.outpost_generation.OutpostGeneration"
    ]
    """<p>Filters the results by Outpost generation. Specify <code>GENERATION_1</code> for first-generation rack deployments or <code>GENERATION_2</code> for second-generation rack deployments.</p>"""
    max_results: NotRequired["capo_outposts.types.max_results1000.MaxResults1000"]
    """<p>The maximum page size.</p>"""
    next_token: NotRequired["capo_outposts.types.token.Token"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrderableInstanceTypesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOrderableInstanceTypesInput:
    out: ListOrderableInstanceTypesInput = {}  # type: ignore[typeddict-item]
    return out
