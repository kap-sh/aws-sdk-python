"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.tag_list


class ListTagsForResourceResponse(TypedDict):
    tag_list: "aws_sdk_cloudhsm.types.tag_list.TagList"
    """<p>One or more tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import aws_sdk_cloudhsm.types.tag_list

    out["TagList"] = aws_sdk_cloudhsm.types.tag_list.serialize_aws_json_1_1(
        value["tag_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import aws_sdk_cloudhsm.types.tag_list

        out["tag_list"] = aws_sdk_cloudhsm.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    else:
        raise DeserializationError("ListTagsForResourceResponse.tag_list required")
    return out
