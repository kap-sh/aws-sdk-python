"""Generated from Smithy shape ``com.amazonaws.opensearch#SecurityLakeDirectQueryDataSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.direct_query_data_source_role_arn


class SecurityLakeDirectQueryDataSource(TypedDict):
    role_arn: "aws_sdk_opensearch.types.direct_query_data_source_role_arn.DirectQueryDataSourceRoleArn"
    """<p> The unique identifier of the IAM role that grants OpenSearch Service permission to access the specified data source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityLakeDirectQueryDataSource) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> SecurityLakeDirectQueryDataSource:
    out: SecurityLakeDirectQueryDataSource = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError(
            "SecurityLakeDirectQueryDataSource.role_arn required"
        )
    return out
