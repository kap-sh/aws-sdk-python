"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListComponentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_visibility_scope
    import capo_greengrassv2.types.default_max_results
    import capo_greengrassv2.types.next_token_string


class ListComponentsRequest(TypedDict, closed=True):
    scope: NotRequired[
        "capo_greengrassv2.types.component_visibility_scope.ComponentVisibilityScope"
    ]
    """<p>The scope of the components to list.</p> <p>Default: <code>PRIVATE</code> </p>"""
    max_results: NotRequired[
        "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
    ]
    """<p>The maximum number of results to be returned per paginated request.</p>"""
    next_token: NotRequired["capo_greengrassv2.types.next_token_string.NextTokenString"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListComponentsRequest:
    out: ListComponentsRequest = {}  # type: ignore[typeddict-item]
    return out
