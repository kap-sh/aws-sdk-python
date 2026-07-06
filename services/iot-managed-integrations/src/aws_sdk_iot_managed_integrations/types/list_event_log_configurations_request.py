"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListEventLogConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token


class ListEventLogConfigurationsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventLogConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventLogConfigurationsRequest:
    out: ListEventLogConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
