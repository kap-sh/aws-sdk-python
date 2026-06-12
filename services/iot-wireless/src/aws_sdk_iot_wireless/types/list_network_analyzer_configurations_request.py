"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListNetworkAnalyzerConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.max_results
    import aws_sdk_iot_wireless.types.next_token


class ListNetworkAnalyzerConfigurationsRequest(TypedDict):
    max_results: "aws_sdk_iot_wireless.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkAnalyzerConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNetworkAnalyzerConfigurationsRequest:
    out: ListNetworkAnalyzerConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
