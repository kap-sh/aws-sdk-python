"""Generated from Smithy shape ``com.amazonaws.proton#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: "aws_sdk_proton.types.tag_list.TagList"
    """<p>A list of resource tags with detail data.</p>"""
    next_token: NotRequired["str"]
    """<p>A token that indicates the location of the next resource tag in the array of resource tags, after the current requested list of resource tags.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.tag_list

    out["tags"] = aws_sdk_proton.types.tag_list.serialize_aws_json_1_0(value["tags"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_proton.types.tag_list

        out["tags"] = aws_sdk_proton.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("ListTagsForResourceOutput.tags required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
