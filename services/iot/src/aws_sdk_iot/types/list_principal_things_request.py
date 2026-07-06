"""Generated from Smithy shape ``com.amazonaws.iot#ListPrincipalThingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.principal
    import aws_sdk_iot.types.registry_max_results


class ListPrincipalThingsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot.types.registry_max_results.RegistryMaxResults"
    ]
    """<p>The maximum number of results to return in this operation.</p>"""
    principal: "aws_sdk_iot.types.principal.Principal"
    """<p>The principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrincipalThingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPrincipalThingsRequest:
    out: ListPrincipalThingsRequest = {}  # type: ignore[typeddict-item]
    return out
