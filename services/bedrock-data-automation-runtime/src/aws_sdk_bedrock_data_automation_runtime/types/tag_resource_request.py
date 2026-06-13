"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.tag_list
    import aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn"
    tags: "aws_sdk_bedrock_data_automation_runtime.types.tag_list.TagList"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import aws_sdk_bedrock_data_automation_runtime.types.tag_list

    out["tags"] = (
        aws_sdk_bedrock_data_automation_runtime.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceARN" in data:
        out["resource_arn"] = data["resourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.tag_list

        out["tags"] = (
            aws_sdk_bedrock_data_automation_runtime.types.tag_list.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
