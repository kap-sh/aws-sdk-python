"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#LogSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.destination
    import aws_sdk_lex_model_building_service.types.kms_key_arn
    import aws_sdk_lex_model_building_service.types.log_type
    import aws_sdk_lex_model_building_service.types.resource_arn


class LogSettingsRequest(TypedDict):
    log_type: "aws_sdk_lex_model_building_service.types.log_type.LogType"
    """<p>The type of logging to enable. Text logs are delivered to a CloudWatch Logs log group. Audio logs are delivered to an S3 bucket.</p>"""
    destination: "aws_sdk_lex_model_building_service.types.destination.Destination"
    """<p>Where the logs will be delivered. Text logs are delivered to a CloudWatch Logs log group. Audio logs are delivered to an S3 bucket.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_lex_model_building_service.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the AWS KMS customer managed key for encrypting audio logs delivered to an S3 bucket. The key does not apply to CloudWatch Logs and is optional for S3 buckets.</p>"""
    resource_arn: "aws_sdk_lex_model_building_service.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the CloudWatch Logs log group or S3 bucket where the logs should be delivered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogSettingsRequest) -> dict:
    out: dict = {}
    import aws_sdk_lex_model_building_service.types.log_type

    out["logType"] = aws_sdk_lex_model_building_service.types.log_type.serialize_json(
        value["log_type"]
    )
    import aws_sdk_lex_model_building_service.types.destination

    out["destination"] = (
        aws_sdk_lex_model_building_service.types.destination.serialize_json(
            value["destination"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> LogSettingsRequest:
    out: LogSettingsRequest = {}  # type: ignore[typeddict-item]
    if "logType" in data:
        import aws_sdk_lex_model_building_service.types.log_type

        out["log_type"] = (
            aws_sdk_lex_model_building_service.types.log_type.deserialize_json(
                data["logType"]
            )
        )
    else:
        raise DeserializationError("LogSettingsRequest.log_type required")
    if "destination" in data:
        import aws_sdk_lex_model_building_service.types.destination

        out["destination"] = (
            aws_sdk_lex_model_building_service.types.destination.deserialize_json(
                data["destination"]
            )
        )
    else:
        raise DeserializationError("LogSettingsRequest.destination required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("LogSettingsRequest.resource_arn required")
    return out
