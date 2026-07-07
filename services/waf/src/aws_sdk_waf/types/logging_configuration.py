"""Generated from Smithy shape ``com.amazonaws.waf#LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.log_destination_configs
    import aws_sdk_waf.types.redacted_fields
    import aws_sdk_waf.types.resource_arn


class LoggingConfiguration(TypedDict, closed=True):
    resource_arn: "aws_sdk_waf.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL that you want to associate with <code>LogDestinationConfigs</code>.</p>"""
    log_destination_configs: (
        "aws_sdk_waf.types.log_destination_configs.LogDestinationConfigs"
    )
    """<p>An array of Amazon Kinesis Data Firehose ARNs.</p>"""
    redacted_fields: NotRequired["aws_sdk_waf.types.redacted_fields.RedactedFields"]
    """<p>The parts of the request that you want redacted from the logs. For example, if you redact the cookie field, the cookie field in the firehose will be <code>xxx</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoggingConfiguration) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_waf.types.log_destination_configs

    out["LogDestinationConfigs"] = (
        aws_sdk_waf.types.log_destination_configs.serialize_aws_json_1_1(
            value["log_destination_configs"]
        )
    )
    if "redacted_fields" in value:
        import aws_sdk_waf.types.redacted_fields

        out["RedactedFields"] = (
            aws_sdk_waf.types.redacted_fields.serialize_aws_json_1_1(
                value["redacted_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("LoggingConfiguration.resource_arn required")
    if "LogDestinationConfigs" in data:
        import aws_sdk_waf.types.log_destination_configs

        out["log_destination_configs"] = (
            aws_sdk_waf.types.log_destination_configs.deserialize_aws_json_1_1(
                data["LogDestinationConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "LoggingConfiguration.log_destination_configs required"
        )
    if "RedactedFields" in data:
        import aws_sdk_waf.types.redacted_fields

        out["redacted_fields"] = (
            aws_sdk_waf.types.redacted_fields.deserialize_aws_json_1_1(
                data["RedactedFields"]
            )
        )
    return out
