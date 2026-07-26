"""Generated from Smithy shape ``com.amazonaws.medialive#CreateEventBridgeRuleTemplateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string_min0_max1024
    import capo_medialive.types.__string_min1_max255_pattern_s
    import capo_medialive.types.__string_min1_max256_pattern_s
    import capo_medialive.types.tag_map


class CreateEventBridgeRuleTemplateGroupRequest(TypedDict, closed=True):
    description: NotRequired[
        "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """A resource's optional description."""
    name: NotRequired[
        "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
    ]
    """A resource's name. Names must be unique within the scope of a resource type in a specific region."""
    tags: NotRequired["capo_medialive.types.tag_map.TagMap"]
    request_id: NotRequired[
        "capo_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
    ]
    """An ID that you assign to a create request. This ID ensures idempotency when creating resources."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventBridgeRuleTemplateGroupRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import capo_medialive.types.tag_map

        out["tags"] = capo_medialive.types.tag_map.serialize_json(value["tags"])
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateEventBridgeRuleTemplateGroupRequest:
    out: CreateEventBridgeRuleTemplateGroupRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import capo_medialive.types.tag_map

        out["tags"] = capo_medialive.types.tag_map.deserialize_json(data["tags"])
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    return out
