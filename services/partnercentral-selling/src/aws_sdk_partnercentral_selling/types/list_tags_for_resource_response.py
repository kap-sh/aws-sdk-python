"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "aws_sdk_partnercentral_selling.types.tag_list.TagList"
    """<p>A map of the key-value pairs for the tag or tags assigned to the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_selling.types.tag_list

    out["Tags"] = aws_sdk_partnercentral_selling.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_partnercentral_selling.types.tag_list

        out["tags"] = (
            aws_sdk_partnercentral_selling.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    return out
