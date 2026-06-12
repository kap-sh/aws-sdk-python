"""Generated from Smithy shape ``com.amazonaws.wafv2#PutLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.logging_configuration


class PutLoggingConfigurationRequest(TypedDict):
    logging_configuration: (
        "aws_sdk_wafv2.types.logging_configuration.LoggingConfiguration"
    )
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLoggingConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.logging_configuration

    out["LoggingConfiguration"] = (
        aws_sdk_wafv2.types.logging_configuration.serialize_aws_json_1_1(
            value["logging_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLoggingConfigurationRequest:
    out: PutLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "LoggingConfiguration" in data:
        import aws_sdk_wafv2.types.logging_configuration

        out["logging_configuration"] = (
            aws_sdk_wafv2.types.logging_configuration.deserialize_aws_json_1_1(
                data["LoggingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutLoggingConfigurationRequest.logging_configuration required"
        )
    return out
