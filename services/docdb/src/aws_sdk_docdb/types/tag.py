"""Generated from Smithy shape ``com.amazonaws.docdb#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.string


class Tag(TypedDict):
    key: NotRequired["aws_sdk_docdb.types.string.String"]
    r"""<p>The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with \"<code>aws:</code>\" or \"<code>rds:</code>\". The string can contain only the set of Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").</p>"""
    value: NotRequired["aws_sdk_docdb.types.string.String"]
    r"""<p>The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with \"<code>aws:</code>\" or \"<code>rds:</code>\". The string can contain only the set of Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").</p>"""


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
