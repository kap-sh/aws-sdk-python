"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteResourceConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_id
    import aws_sdk_config_service.types.resource_type_string


class DeleteResourceConfigRequest(TypedDict):
    resource_type: (
        "aws_sdk_config_service.types.resource_type_string.ResourceTypeString"
    )
    """<p>The type of the resource.</p>"""
    resource_id: "aws_sdk_config_service.types.resource_id.ResourceId"
    """<p>Unique identifier of the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourceConfigRequest) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourceConfigRequest:
    out: DeleteResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("DeleteResourceConfigRequest.resource_type required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("DeleteResourceConfigRequest.resource_id required")
    return out
