"""Generated from Smithy shape ``com.amazonaws.cloudformation#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.tag_key
    import aws_sdk_cloudformation.types.tag_value


class Tag(TypedDict):
    key: NotRequired["aws_sdk_cloudformation.types.tag_key.TagKey"]
    """<p>A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services have the reserved prefix: <code>aws:</code>.</p>"""
    value: NotRequired["aws_sdk_cloudformation.types.tag_value.TagValue"]
    """<p>A string that contains the value for this tag. You can specify a maximum of 256 characters for a tag value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Tag, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "key" in value:
        pairs.append((f"{prefix}.Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
