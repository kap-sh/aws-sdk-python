"""Generated from Smithy shape ``com.amazonaws.iot#ListV2LoggingLevelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.log_target_type
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.skyfall_max_results


class ListV2LoggingLevelsRequest(TypedDict):
    target_type: NotRequired["aws_sdk_iot.types.log_target_type.LogTargetType"]
    """<p>The type of resource for which you are configuring logging. Must be <code>THING_Group</code>.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.skyfall_max_results.SkyfallMaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListV2LoggingLevelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListV2LoggingLevelsRequest:
    out: ListV2LoggingLevelsRequest = {}  # type: ignore[typeddict-item]
    return out
