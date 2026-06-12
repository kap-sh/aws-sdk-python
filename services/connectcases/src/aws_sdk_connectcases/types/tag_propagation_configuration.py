"""Generated from Smithy shape ``com.amazonaws.connectcases#TagPropagationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.mutable_tags
    import aws_sdk_connectcases.types.tag_propagation_resource_type


class TagPropagationConfiguration(TypedDict):
    resource_type: "aws_sdk_connectcases.types.tag_propagation_resource_type.TagPropagationResourceType"
    """<p>Supported resource types for tag propagation. Determines which resources will receive automatically propagated tags.</p>"""
    tag_map: "aws_sdk_connectcases.types.mutable_tags.MutableTags"
    """<p>The tags that will be applied to the created resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagPropagationConfiguration) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    import aws_sdk_connectcases.types.mutable_tags

    out["tagMap"] = aws_sdk_connectcases.types.mutable_tags.serialize_json(
        value["tag_map"]
    )
    return out


def deserialize_json(data: dict) -> TagPropagationConfiguration:
    out: TagPropagationConfiguration = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("TagPropagationConfiguration.resource_type required")
    if "tagMap" in data:
        import aws_sdk_connectcases.types.mutable_tags

        out["tag_map"] = aws_sdk_connectcases.types.mutable_tags.deserialize_json(
            data["tagMap"]
        )
    else:
        raise DeserializationError("TagPropagationConfiguration.tag_map required")
    return out
