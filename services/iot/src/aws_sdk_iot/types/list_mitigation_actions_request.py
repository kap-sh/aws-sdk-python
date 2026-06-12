"""Generated from Smithy shape ``com.amazonaws.iot#ListMitigationActionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.mitigation_action_type
    import aws_sdk_iot.types.next_token


class ListMitigationActionsRequest(TypedDict):
    action_type: NotRequired[
        "aws_sdk_iot.types.mitigation_action_type.MitigationActionType"
    ]
    """<p>Specify a value to limit the result to mitigation actions with a specific action type.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 25.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMitigationActionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMitigationActionsRequest:
    out: ListMitigationActionsRequest = {}  # type: ignore[typeddict-item]
    return out
