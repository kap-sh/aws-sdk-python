"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#LogSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.destination
    import aws_sdk_lex_model_building_service.types.kms_key_arn
    import aws_sdk_lex_model_building_service.types.log_type
    import aws_sdk_lex_model_building_service.types.resource_arn
    import aws_sdk_lex_model_building_service.types.resource_prefix


class LogSettingsResponse(TypedDict):
    log_type: NotRequired["aws_sdk_lex_model_building_service.types.log_type.LogType"]
    """<p>The type of logging that is enabled.</p>"""
    destination: NotRequired[
        "aws_sdk_lex_model_building_service.types.destination.Destination"
    ]
    """<p>The destination where logs are delivered.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_lex_model_building_service.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the key used to encrypt audio logs in an S3 bucket.</p>"""
    resource_arn: NotRequired[
        "aws_sdk_lex_model_building_service.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch Logs log group or S3 bucket where the logs are delivered.</p>"""
    resource_prefix: NotRequired[
        "aws_sdk_lex_model_building_service.types.resource_prefix.ResourcePrefix"
    ]
    """<p>The resource prefix is the first part of the S3 object key within the S3 bucket that you specified to contain audio logs. For CloudWatch Logs it is the prefix of the log stream name within the log group that you specified. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogSettingsResponse) -> dict:
    out: dict = {}
    if "log_type" in value:
        import aws_sdk_lex_model_building_service.types.log_type

        out["logType"] = (
            aws_sdk_lex_model_building_service.types.log_type.serialize_json(
                value["log_type"]
            )
        )
    if "destination" in value:
        import aws_sdk_lex_model_building_service.types.destination

        out["destination"] = (
            aws_sdk_lex_model_building_service.types.destination.serialize_json(
                value["destination"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_prefix" in value:
        out["resourcePrefix"] = value["resource_prefix"]
    return out


def deserialize_json(data: dict) -> LogSettingsResponse:
    out: LogSettingsResponse = {}  # type: ignore[typeddict-item]
    if "logType" in data:
        import aws_sdk_lex_model_building_service.types.log_type

        out["log_type"] = (
            aws_sdk_lex_model_building_service.types.log_type.deserialize_json(
                data["logType"]
            )
        )
    if "destination" in data:
        import aws_sdk_lex_model_building_service.types.destination

        out["destination"] = (
            aws_sdk_lex_model_building_service.types.destination.deserialize_json(
                data["destination"]
            )
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "resourcePrefix" in data:
        out["resource_prefix"] = data["resourcePrefix"]
    return out
