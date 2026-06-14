"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#S3TablesIntegration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.s3_tables_datasource_name
    import aws_sdk_cloudwatch_logs.types.s3_tables_datasource_type


class S3TablesIntegration(TypedDict):
    datasource_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.s3_tables_datasource_name.S3TablesDatasourceName"
    ]
    """<p>The name of the S3 Tables datasource.</p>"""
    datasource_type: NotRequired[
        "aws_sdk_cloudwatch_logs.types.s3_tables_datasource_type.S3TablesDatasourceType"
    ]
    """<p>The type of the S3 Tables datasource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TablesIntegration) -> dict:
    out: dict = {}
    if "datasource_name" in value:
        out["datasourceName"] = value["datasource_name"]
    if "datasource_type" in value:
        out["datasourceType"] = value["datasource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3TablesIntegration:
    out: S3TablesIntegration = {}  # type: ignore[typeddict-item]
    if "datasourceName" in data:
        out["datasource_name"] = data["datasourceName"]
    if "datasourceType" in data:
        out["datasource_type"] = data["datasourceType"]
    return out
