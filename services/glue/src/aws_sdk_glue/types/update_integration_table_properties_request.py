"""Generated from Smithy shape ``com.amazonaws.glue#UpdateIntegrationTablePropertiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.source_table_config
    import aws_sdk_glue.types.string128
    import aws_sdk_glue.types.string512
    import aws_sdk_glue.types.target_table_config


class UpdateIntegrationTablePropertiesRequest(TypedDict):
    resource_arn: "aws_sdk_glue.types.string512.String512"
    """<p>The connection ARN of the source, or the database ARN of the target.</p>"""
    table_name: "aws_sdk_glue.types.string128.String128"
    """<p>The name of the table to be replicated.</p>"""
    source_table_config: NotRequired[
        "aws_sdk_glue.types.source_table_config.SourceTableConfig"
    ]
    """<p>A structure for the source table configuration.</p>"""
    target_table_config: NotRequired[
        "aws_sdk_glue.types.target_table_config.TargetTableConfig"
    ]
    """<p>A structure for the target table configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIntegrationTablePropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["TableName"] = value["table_name"]
    if "source_table_config" in value:
        import aws_sdk_glue.types.source_table_config

        out["SourceTableConfig"] = (
            aws_sdk_glue.types.source_table_config.serialize_aws_json_1_1(
                value["source_table_config"]
            )
        )
    if "target_table_config" in value:
        import aws_sdk_glue.types.target_table_config

        out["TargetTableConfig"] = (
            aws_sdk_glue.types.target_table_config.serialize_aws_json_1_1(
                value["target_table_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIntegrationTablePropertiesRequest:
    out: UpdateIntegrationTablePropertiesRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "UpdateIntegrationTablePropertiesRequest.resource_arn required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "UpdateIntegrationTablePropertiesRequest.table_name required"
        )
    if "SourceTableConfig" in data:
        import aws_sdk_glue.types.source_table_config

        out["source_table_config"] = (
            aws_sdk_glue.types.source_table_config.deserialize_aws_json_1_1(
                data["SourceTableConfig"]
            )
        )
    if "TargetTableConfig" in data:
        import aws_sdk_glue.types.target_table_config

        out["target_table_config"] = (
            aws_sdk_glue.types.target_table_config.deserialize_aws_json_1_1(
                data["TargetTableConfig"]
            )
        )
    return out
