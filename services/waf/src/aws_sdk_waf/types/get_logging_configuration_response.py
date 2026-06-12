"""Generated from Smithy shape ``com.amazonaws.waf#GetLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf.types.logging_configuration


class GetLoggingConfigurationResponse(TypedDict):
    logging_configuration: NotRequired[
        "aws_sdk_waf.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The <a>LoggingConfiguration</a> for the specified web ACL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLoggingConfigurationResponse) -> dict:
    out: dict = {}
    if "logging_configuration" in value:
        import aws_sdk_waf.types.logging_configuration

        out["LoggingConfiguration"] = (
            aws_sdk_waf.types.logging_configuration.serialize_aws_json_1_1(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLoggingConfigurationResponse:
    out: GetLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LoggingConfiguration" in data:
        import aws_sdk_waf.types.logging_configuration

        out["logging_configuration"] = (
            aws_sdk_waf.types.logging_configuration.deserialize_aws_json_1_1(
                data["LoggingConfiguration"]
            )
        )
    return out
