"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupErrorDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_id
    import aws_sdk_opensearchserverless.types.collection_group_name


class CollectionGroupErrorDetail(TypedDict):
    id: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_id.CollectionGroupId"
    ]
    """<p>If the request contains collection group IDs, the response includes the IDs provided in the request.</p>"""
    name: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName"
    ]
    """<p>If the request contains collection group names, the response includes the names provided in the request.</p>"""
    error_message: NotRequired["str"]
    """<p>A description of the error. For example, <code>The specified Collection Group is not found.</code> </p>"""
    error_code: NotRequired["str"]
    """<p>The error code for the request. For example, <code>NOT_FOUND</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupErrorDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CollectionGroupErrorDetail:
    out: CollectionGroupErrorDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    return out
