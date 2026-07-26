"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.taggable_resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceARN" in data:
        out["resource_arn"] = data["resourceARN"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
