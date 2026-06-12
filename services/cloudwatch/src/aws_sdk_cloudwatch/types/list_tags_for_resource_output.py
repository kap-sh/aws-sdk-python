"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.tag_list


class ListTagsForResourceOutput(TypedDict):
    tags: NotRequired["aws_sdk_cloudwatch.types.tag_list.TagList"]
    """<p>The list of tag keys and values associated with the resource you specified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_cloudwatch.types.tag_list

        out["Tags"] = aws_sdk_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_cloudwatch.types.tag_list

        out["tags"] = aws_sdk_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTagsForResourceOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "tags" in value:
        import aws_sdk_cloudwatch.types.tag_list

        aws_sdk_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudwatch.types.tag_list

        out["tags"] = aws_sdk_cloudwatch.types.tag_list.deserialize_query(child_tags)
    return out
