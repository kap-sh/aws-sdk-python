"""Generated from Smithy shape ``com.amazonaws.configservice#StoredQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.query_arn
    import aws_sdk_config_service.types.query_description
    import aws_sdk_config_service.types.query_expression
    import aws_sdk_config_service.types.query_id
    import aws_sdk_config_service.types.query_name


class StoredQuery(TypedDict):
    query_id: NotRequired["aws_sdk_config_service.types.query_id.QueryId"]
    """<p>The ID of the query.</p>"""
    query_arn: NotRequired["aws_sdk_config_service.types.query_arn.QueryArn"]
    """<p>Amazon Resource Name (ARN) of the query. For example, arn:partition:service:region:account-id:resource-type/resource-name/resource-id.</p>"""
    query_name: "aws_sdk_config_service.types.query_name.QueryName"
    """<p>The name of the query.</p>"""
    description: NotRequired[
        "aws_sdk_config_service.types.query_description.QueryDescription"
    ]
    """<p>A unique description for the query.</p>"""
    expression: NotRequired[
        "aws_sdk_config_service.types.query_expression.QueryExpression"
    ]
    """<p>The expression of the query. For example, <code>SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StoredQuery) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "query_arn" in value:
        out["QueryArn"] = value["query_arn"]
    out["QueryName"] = value["query_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "expression" in value:
        out["Expression"] = value["expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StoredQuery:
    out: StoredQuery = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    if "QueryArn" in data:
        out["query_arn"] = data["QueryArn"]
    if "QueryName" in data:
        out["query_name"] = data["QueryName"]
    else:
        raise DeserializationError("StoredQuery.query_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    return out
