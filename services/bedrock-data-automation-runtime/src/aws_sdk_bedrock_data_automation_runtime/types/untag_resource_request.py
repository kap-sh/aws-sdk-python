"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.tag_key_list
    import aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn"
    tag_keys: "aws_sdk_bedrock_data_automation_runtime.types.tag_key_list.TagKeyList"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import aws_sdk_bedrock_data_automation_runtime.types.tag_key_list

    out["tagKeys"] = (
        aws_sdk_bedrock_data_automation_runtime.types.tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceARN" in data:
        out["resource_arn"] = data["resourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_bedrock_data_automation_runtime.types.tag_key_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
