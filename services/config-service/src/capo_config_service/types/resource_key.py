"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.resource_id
    import capo_config_service.types.resource_type


class ResourceKey(TypedDict, closed=True):
    resource_type: "capo_config_service.types.resource_type.ResourceType"
    """<p>The resource type.</p>"""
    resource_id: "capo_config_service.types.resource_id.ResourceId"
    """<p>The ID of the resource (for example., sg-xxxxxx). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceKey) -> dict:
    out: dict = {}
    import capo_config_service.types.resource_type

    out["resourceType"] = (
        capo_config_service.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    out["resourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceKey:
    out: ResourceKey = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import capo_config_service.types.resource_type

        out["resource_type"] = (
            capo_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError("ResourceKey.resource_type required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ResourceKey.resource_id required")
    return out
