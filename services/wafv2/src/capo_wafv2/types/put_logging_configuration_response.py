"""Generated from Smithy shape ``com.amazonaws.wafv2#PutLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.logging_configuration


class PutLoggingConfigurationResponse(TypedDict, closed=True):
    logging_configuration: NotRequired[
        "capo_wafv2.types.logging_configuration.LoggingConfiguration"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLoggingConfigurationResponse) -> dict:
    out: dict = {}
    if "logging_configuration" in value:
        import capo_wafv2.types.logging_configuration

        out["LoggingConfiguration"] = (
            capo_wafv2.types.logging_configuration.serialize_aws_json_1_1(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLoggingConfigurationResponse:
    out: PutLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LoggingConfiguration" in data:
        import capo_wafv2.types.logging_configuration

        out["logging_configuration"] = (
            capo_wafv2.types.logging_configuration.deserialize_aws_json_1_1(
                data["LoggingConfiguration"]
            )
        )
    return out
