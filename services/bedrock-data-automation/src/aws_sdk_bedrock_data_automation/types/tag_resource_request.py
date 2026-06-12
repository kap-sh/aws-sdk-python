"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.tag_list
    import aws_sdk_bedrock_data_automation.types.taggable_resource_arn


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_bedrock_data_automation.types.taggable_resource_arn.TaggableResourceArn"
    tags: "aws_sdk_bedrock_data_automation.types.tag_list.TagList"


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import aws_sdk_bedrock_data_automation.types.tag_list

    out["tags"] = aws_sdk_bedrock_data_automation.types.tag_list.serialize_json(
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
        import aws_sdk_bedrock_data_automation.types.tag_list

        out["tags"] = aws_sdk_bedrock_data_automation.types.tag_list.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
