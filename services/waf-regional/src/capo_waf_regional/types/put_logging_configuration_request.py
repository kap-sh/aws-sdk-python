"""Generated from Smithy shape ``com.amazonaws.wafregional#PutLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.logging_configuration


class PutLoggingConfigurationRequest(TypedDict, closed=True):
    logging_configuration: (
        "capo_waf_regional.types.logging_configuration.LoggingConfiguration"
    )
    """<p>The Amazon Kinesis Data Firehose that contains the inspected traffic information, the redacted fields details, and the Amazon Resource Name (ARN) of the web ACL to monitor.</p> <note> <p>When specifying <code>Type</code> in <code>RedactedFields</code>, you must use one of the following values: <code>URI</code>, <code>QUERY_STRING</code>, <code>HEADER</code>, or <code>METHOD</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLoggingConfigurationRequest) -> dict:
    out: dict = {}
    import capo_waf_regional.types.logging_configuration

    out["LoggingConfiguration"] = (
        capo_waf_regional.types.logging_configuration.serialize_aws_json_1_1(
            value["logging_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLoggingConfigurationRequest:
    out: PutLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "LoggingConfiguration" in data:
        import capo_waf_regional.types.logging_configuration

        out["logging_configuration"] = (
            capo_waf_regional.types.logging_configuration.deserialize_aws_json_1_1(
                data["LoggingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutLoggingConfigurationRequest.logging_configuration required"
        )
    return out
