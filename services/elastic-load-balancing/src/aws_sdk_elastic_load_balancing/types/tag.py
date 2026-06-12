"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.tag_key
    import aws_sdk_elastic_load_balancing.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_elastic_load_balancing.types.tag_key.TagKey"
    """<p>The key of the tag.</p>"""
    value: NotRequired["aws_sdk_elastic_load_balancing.types.tag_value.TagValue"]
    """<p>The value of the tag.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Tag, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((f"{prefix}.Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    else:
        raise DeserializationError("Tag.key required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
