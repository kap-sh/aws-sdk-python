"""Generated from Smithy shape ``com.amazonaws.configservice#StoredQueryMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.query_arn
    import aws_sdk_config_service.types.query_description
    import aws_sdk_config_service.types.query_id
    import aws_sdk_config_service.types.query_name


class StoredQueryMetadata(TypedDict):
    query_id: "aws_sdk_config_service.types.query_id.QueryId"
    """<p>The ID of the query. </p>"""
    query_arn: "aws_sdk_config_service.types.query_arn.QueryArn"
    """<p>Amazon Resource Name (ARN) of the query. For example, arn:partition:service:region:account-id:resource-type/resource-name/resource-id.</p>"""
    query_name: "aws_sdk_config_service.types.query_name.QueryName"
    """<p>The name of the query.</p>"""
    description: NotRequired[
        "aws_sdk_config_service.types.query_description.QueryDescription"
    ]
    """<p>A unique description for the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StoredQueryMetadata) -> dict:
    out: dict = {}
    out["QueryId"] = value["query_id"]
    out["QueryArn"] = value["query_arn"]
    out["QueryName"] = value["query_name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StoredQueryMetadata:
    out: StoredQueryMetadata = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    else:
        raise DeserializationError("StoredQueryMetadata.query_id required")
    if "QueryArn" in data:
        out["query_arn"] = data["QueryArn"]
    else:
        raise DeserializationError("StoredQueryMetadata.query_arn required")
    if "QueryName" in data:
        out["query_name"] = data["QueryName"]
    else:
        raise DeserializationError("StoredQueryMetadata.query_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    return out
