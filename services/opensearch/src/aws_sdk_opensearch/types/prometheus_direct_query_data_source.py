"""Generated from Smithy shape ``com.amazonaws.opensearch#PrometheusDirectQueryDataSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.amp_workspace_arn
    import aws_sdk_opensearch.types.direct_query_data_source_role_arn


class PrometheusDirectQueryDataSource(TypedDict):
    role_arn: "aws_sdk_opensearch.types.direct_query_data_source_role_arn.DirectQueryDataSourceRoleArn"
    """<p> The unique identifier of the IAM role that grants OpenSearch Service permission to access the specified data source. </p>"""
    workspace_arn: "aws_sdk_opensearch.types.amp_workspace_arn.AMPWorkspaceArn"
    """<p> The unique identifier of the Amazon Managed Prometheus Workspace that is associated with the specified data source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrometheusDirectQueryDataSource) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    out["WorkspaceArn"] = value["workspace_arn"]
    return out


def deserialize_json(data: dict) -> PrometheusDirectQueryDataSource:
    out: PrometheusDirectQueryDataSource = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("PrometheusDirectQueryDataSource.role_arn required")
    if "WorkspaceArn" in data:
        out["workspace_arn"] = data["WorkspaceArn"]
    else:
        raise DeserializationError(
            "PrometheusDirectQueryDataSource.workspace_arn required"
        )
    return out
