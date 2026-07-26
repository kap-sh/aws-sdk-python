"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.tag_list
    import capo_bedrock_data_automation.types.taggable_resource_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_bedrock_data_automation.types.taggable_resource_arn.TaggableResourceArn"
    )
    tags: "capo_bedrock_data_automation.types.tag_list.TagList"


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import capo_bedrock_data_automation.types.tag_list

    out["tags"] = capo_bedrock_data_automation.types.tag_list.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceARN" in data:
        out["resource_arn"] = data["resourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import capo_bedrock_data_automation.types.tag_list

        out["tags"] = capo_bedrock_data_automation.types.tag_list.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
