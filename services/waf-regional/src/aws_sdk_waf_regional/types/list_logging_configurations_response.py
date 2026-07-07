"""Generated from Smithy shape ``com.amazonaws.wafregional#ListLoggingConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.logging_configurations
    import aws_sdk_waf_regional.types.next_marker


class ListLoggingConfigurationsResponse(TypedDict, closed=True):
    logging_configurations: NotRequired[
        "aws_sdk_waf_regional.types.logging_configurations.LoggingConfigurations"
    ]
    """<p>An array of <a>LoggingConfiguration</a> objects.</p>"""
    next_marker: NotRequired["aws_sdk_waf_regional.types.next_marker.NextMarker"]
    """<p>If you have more <code>LoggingConfigurations</code> than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>LoggingConfigurations</code>, submit another <code>ListLoggingConfigurations</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLoggingConfigurationsResponse) -> dict:
    out: dict = {}
    if "logging_configurations" in value:
        import aws_sdk_waf_regional.types.logging_configurations

        out["LoggingConfigurations"] = (
            aws_sdk_waf_regional.types.logging_configurations.serialize_aws_json_1_1(
                value["logging_configurations"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLoggingConfigurationsResponse:
    out: ListLoggingConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "LoggingConfigurations" in data:
        import aws_sdk_waf_regional.types.logging_configurations

        out["logging_configurations"] = (
            aws_sdk_waf_regional.types.logging_configurations.deserialize_aws_json_1_1(
                data["LoggingConfigurations"]
            )
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
