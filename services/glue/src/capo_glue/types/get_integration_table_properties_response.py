"""Generated from Smithy shape ``com.amazonaws.glue#GetIntegrationTablePropertiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.source_table_config
    import capo_glue.types.string128
    import capo_glue.types.string512
    import capo_glue.types.target_table_config


class GetIntegrationTablePropertiesResponse(TypedDict, closed=True):
    resource_arn: NotRequired["capo_glue.types.string512.String512"]
    """<p>The Amazon Resource Name (ARN) of the target table for which to retrieve integration table properties. Currently, this API only supports retrieving properties for target tables, and the provided ARN should be the ARN of the target table in the Glue Data Catalog. Support for retrieving integration table properties for source connections (using the connection ARN) is not yet implemented and will be added in a future release. </p>"""
    table_name: NotRequired["capo_glue.types.string128.String128"]
    """<p>The name of the table to be replicated.</p>"""
    source_table_config: NotRequired[
        "capo_glue.types.source_table_config.SourceTableConfig"
    ]
    """<p>A structure for the source table configuration.</p>"""
    target_table_config: NotRequired[
        "capo_glue.types.target_table_config.TargetTableConfig"
    ]
    """<p>A structure for the target table configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIntegrationTablePropertiesResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "source_table_config" in value:
        import capo_glue.types.source_table_config

        out["SourceTableConfig"] = (
            capo_glue.types.source_table_config.serialize_aws_json_1_1(
                value["source_table_config"]
            )
        )
    if "target_table_config" in value:
        import capo_glue.types.target_table_config

        out["TargetTableConfig"] = (
            capo_glue.types.target_table_config.serialize_aws_json_1_1(
                value["target_table_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIntegrationTablePropertiesResponse:
    out: GetIntegrationTablePropertiesResponse = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "SourceTableConfig" in data:
        import capo_glue.types.source_table_config

        out["source_table_config"] = (
            capo_glue.types.source_table_config.deserialize_aws_json_1_1(
                data["SourceTableConfig"]
            )
        )
    if "TargetTableConfig" in data:
        import capo_glue.types.target_table_config

        out["target_table_config"] = (
            capo_glue.types.target_table_config.deserialize_aws_json_1_1(
                data["TargetTableConfig"]
            )
        )
    return out
