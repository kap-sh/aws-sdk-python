"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListPositionConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.max_results
    import aws_sdk_iot_wireless.types.next_token
    import aws_sdk_iot_wireless.types.position_resource_type


class ListPositionConfigurationsRequest(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType"
    ]
    """<p>Resource type for which position configurations are listed.</p>"""
    max_results: "aws_sdk_iot_wireless.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPositionConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPositionConfigurationsRequest:
    out: ListPositionConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
