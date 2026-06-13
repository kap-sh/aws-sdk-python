"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateKnowledgeBasePermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.knowledge_base_arn
    import aws_sdk_quicksight.types.knowledge_base_id
    import aws_sdk_quicksight.types.resource_permission_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateKnowledgeBasePermissionsResponse(TypedDict):
    knowledge_base_arn: "aws_sdk_quicksight.types.knowledge_base_arn.KnowledgeBaseArn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier for the knowledge base.</p>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The resource permissions for the knowledge base.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.status_code.StatusCode"]
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKnowledgeBasePermissionsResponse) -> dict:
    out: dict = {}
    out["KnowledgeBaseArn"] = value["knowledge_base_arn"]
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    if "permissions" in value:
        import aws_sdk_quicksight.types.resource_permission_list

        out["Permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateKnowledgeBasePermissionsResponse:
    out: UpdateKnowledgeBasePermissionsResponse = {}  # type: ignore[typeddict-item]
    if "KnowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["KnowledgeBaseArn"]
    else:
        raise DeserializationError(
            "UpdateKnowledgeBasePermissionsResponse.knowledge_base_arn required"
        )
    if "KnowledgeBaseId" in data:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        raise DeserializationError(
            "UpdateKnowledgeBasePermissionsResponse.knowledge_base_id required"
        )
    if "Permissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
