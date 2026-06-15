"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.tag_list


class ListTagsForResourceResponse(TypedDict):
    tags: "aws_sdk_mailmanager.types.tag_list.TagList"
    r"""<p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.tag_list

    out["Tags"] = aws_sdk_mailmanager.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_mailmanager.types.tag_list

        out["tags"] = aws_sdk_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    return out
