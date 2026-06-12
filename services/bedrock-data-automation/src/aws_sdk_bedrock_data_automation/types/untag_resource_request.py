"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.tag_key_list
    import aws_sdk_bedrock_data_automation.types.taggable_resource_arn


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_bedrock_data_automation.types.taggable_resource_arn.TaggableResourceArn"
    tag_keys: "aws_sdk_bedrock_data_automation.types.tag_key_list.TagKeyList"


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import aws_sdk_bedrock_data_automation.types.tag_key_list

    out["tagKeys"] = aws_sdk_bedrock_data_automation.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceARN" in data:
        out["resource_arn"] = data["resourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_bedrock_data_automation.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_bedrock_data_automation.types.tag_key_list.deserialize_json(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
