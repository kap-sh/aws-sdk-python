"""Generated from Smithy shape ``com.amazonaws.wafv2#ListLoggingConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.logging_configurations
    import aws_sdk_wafv2.types.next_marker


class ListLoggingConfigurationsResponse(TypedDict):
    logging_configurations: NotRequired[
        "aws_sdk_wafv2.types.logging_configurations.LoggingConfigurations"
    ]
    """<p>Array of logging configurations. If you specified a <code>Limit</code> in your request, this might not be the full list. </p>"""
    next_marker: NotRequired["aws_sdk_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLoggingConfigurationsResponse) -> dict:
    out: dict = {}
    if "logging_configurations" in value:
        import aws_sdk_wafv2.types.logging_configurations

        out["LoggingConfigurations"] = (
            aws_sdk_wafv2.types.logging_configurations.serialize_aws_json_1_1(
                value["logging_configurations"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLoggingConfigurationsResponse:
    out: ListLoggingConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "LoggingConfigurations" in data:
        import aws_sdk_wafv2.types.logging_configurations

        out["logging_configurations"] = (
            aws_sdk_wafv2.types.logging_configurations.deserialize_aws_json_1_1(
                data["LoggingConfigurations"]
            )
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
