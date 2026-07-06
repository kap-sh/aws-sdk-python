"""Generated from Smithy shape ``com.amazonaws.redshift#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class Tag(TypedDict, closed=True):
    key: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The key, or name, for the resource tag.</p>"""
    value: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The value for the resource tag.</p>"""


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
