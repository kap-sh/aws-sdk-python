"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_bedrock_data_automation_runtime.types.tag_list.TagList"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_bedrock_data_automation_runtime.types.tag_list

        out["tags"] = (
            capo_bedrock_data_automation_runtime.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_bedrock_data_automation_runtime.types.tag_list

        out["tags"] = (
            capo_bedrock_data_automation_runtime.types.tag_list.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    return out
