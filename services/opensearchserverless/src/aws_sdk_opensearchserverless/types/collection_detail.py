"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_name
    import aws_sdk_opensearchserverless.types.collection_id
    import aws_sdk_opensearchserverless.types.collection_name
    import aws_sdk_opensearchserverless.types.collection_status
    import aws_sdk_opensearchserverless.types.collection_type
    import aws_sdk_opensearchserverless.types.deletion_protection
    import aws_sdk_opensearchserverless.types.fips_endpoints
    import aws_sdk_opensearchserverless.types.standby_replicas
    import aws_sdk_opensearchserverless.types.vector_options


class CollectionDetail(TypedDict):
    id: NotRequired["aws_sdk_opensearchserverless.types.collection_id.CollectionId"]
    """<p>A unique identifier for the collection.</p>"""
    name: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_name.CollectionName"
    ]
    """<p>The name of the collection.</p>"""
    status: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_status.CollectionStatus"
    ]
    """<p>The current status of the collection.</p>"""
    type: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_type.CollectionType"
    ]
    """<p>The type of collection.</p>"""
    description: NotRequired["str"]
    """<p>A description of the collection.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the collection.</p>"""
    kms_key_arn: NotRequired["str"]
    """<p>The ARN of the Amazon Web Services KMS key used to encrypt the collection.</p>"""
    standby_replicas: NotRequired[
        "aws_sdk_opensearchserverless.types.standby_replicas.StandbyReplicas"
    ]
    """<p>Details about an OpenSearch Serverless collection.</p>"""
    deletion_protection: NotRequired[
        "aws_sdk_opensearchserverless.types.deletion_protection.DeletionProtection"
    ]
    """<p>Indicates whether deletion protection is <code>ENABLED</code> or <code>DISABLED</code> for the collection.</p>"""
    vector_options: NotRequired[
        "aws_sdk_opensearchserverless.types.vector_options.VectorOptions"
    ]
    """<p>Configuration options for vector search capabilities in the collection.</p>"""
    created_date: NotRequired["int"]
    """<p>The Epoch time when the collection was created.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The date and time when the collection was last modified.</p>"""
    collection_endpoint: NotRequired["str"]
    """<p>Collection-specific endpoint used to submit index, search, and data upload requests to an OpenSearch Serverless collection.</p>"""
    dashboard_endpoint: NotRequired["str"]
    """<p>Collection-specific endpoint used to access OpenSearch Dashboards.</p>"""
    fips_endpoints: NotRequired[
        "aws_sdk_opensearchserverless.types.fips_endpoints.FipsEndpoints"
    ]
    """<p>FIPS-compliant endpoints for the collection. These endpoints use FIPS 140-3 validated cryptographic modules and are required for federal government workloads that must comply with FedRAMP security standards.</p>"""
    failure_code: NotRequired["str"]
    """<p>A failure code associated with the request.</p>"""
    failure_message: NotRequired["str"]
    """<p>A message associated with the failure code.</p>"""
    collection_group_name: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName"
    ]
    """<p>The name of the collection group that contains this collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "type" in value:
        out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "standby_replicas" in value:
        out["standbyReplicas"] = value["standby_replicas"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "vector_options" in value:
        import aws_sdk_opensearchserverless.types.vector_options

        out["vectorOptions"] = (
            aws_sdk_opensearchserverless.types.vector_options.serialize_aws_json_1_0(
                value["vector_options"]
            )
        )
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    if "collection_endpoint" in value:
        out["collectionEndpoint"] = value["collection_endpoint"]
    if "dashboard_endpoint" in value:
        out["dashboardEndpoint"] = value["dashboard_endpoint"]
    if "fips_endpoints" in value:
        import aws_sdk_opensearchserverless.types.fips_endpoints

        out["fipsEndpoints"] = (
            aws_sdk_opensearchserverless.types.fips_endpoints.serialize_aws_json_1_0(
                value["fips_endpoints"]
            )
        )
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "collection_group_name" in value:
        out["collectionGroupName"] = value["collection_group_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CollectionDetail:
    out: CollectionDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "type" in data:
        out["type"] = data["type"]
    if "description" in data:
        out["description"] = data["description"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "standbyReplicas" in data:
        out["standby_replicas"] = data["standbyReplicas"]
    if "deletionProtection" in data:
        out["deletion_protection"] = data["deletionProtection"]
    if "vectorOptions" in data:
        import aws_sdk_opensearchserverless.types.vector_options

        out["vector_options"] = (
            aws_sdk_opensearchserverless.types.vector_options.deserialize_aws_json_1_0(
                data["vectorOptions"]
            )
        )
    if "createdDate" in data:
        out["created_date"] = data["createdDate"]
    if "lastModifiedDate" in data:
        out["last_modified_date"] = data["lastModifiedDate"]
    if "collectionEndpoint" in data:
        out["collection_endpoint"] = data["collectionEndpoint"]
    if "dashboardEndpoint" in data:
        out["dashboard_endpoint"] = data["dashboardEndpoint"]
    if "fipsEndpoints" in data:
        import aws_sdk_opensearchserverless.types.fips_endpoints

        out["fips_endpoints"] = (
            aws_sdk_opensearchserverless.types.fips_endpoints.deserialize_aws_json_1_0(
                data["fipsEndpoints"]
            )
        )
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "collectionGroupName" in data:
        out["collection_group_name"] = data["collectionGroupName"]
    return out
