"""Generated from Smithy shape ``com.amazonaws.opensearch#DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.arn
    import aws_sdk_opensearch.types.data_source_description
    import aws_sdk_opensearch.types.role_arn


class DataSource(TypedDict, closed=True):
    data_source_arn: NotRequired["aws_sdk_opensearch.types.arn.ARN"]
    data_source_description: NotRequired[
        "aws_sdk_opensearch.types.data_source_description.DataSourceDescription"
    ]
    """<p>Detailed description of a data source.</p>"""
    iam_role_for_data_source_arn: NotRequired[
        "aws_sdk_opensearch.types.role_arn.RoleArn"
    ]
    """<p>The ARN of the IAM role to be used for cross account/region data source association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSource) -> dict:
    out: dict = {}
    if "data_source_arn" in value:
        out["dataSourceArn"] = value["data_source_arn"]
    if "data_source_description" in value:
        out["dataSourceDescription"] = value["data_source_description"]
    if "iam_role_for_data_source_arn" in value:
        out["iamRoleForDataSourceArn"] = value["iam_role_for_data_source_arn"]
    return out


def deserialize_json(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "dataSourceArn" in data:
        out["data_source_arn"] = data["dataSourceArn"]
    if "dataSourceDescription" in data:
        out["data_source_description"] = data["dataSourceDescription"]
    if "iamRoleForDataSourceArn" in data:
        out["iam_role_for_data_source_arn"] = data["iamRoleForDataSourceArn"]
    return out
