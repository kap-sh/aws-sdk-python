"""Generated from Smithy shape ``com.amazonaws.xray#Alias``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.alias_names
    import aws_sdk_xray.types.string


class Alias(TypedDict):
    name: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The canonical name of the alias.</p>"""
    names: NotRequired["aws_sdk_xray.types.alias_names.AliasNames"]
    """<p>A list of names for the alias, including the canonical name.</p>"""
    type: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The type of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Alias) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "names" in value:
        import aws_sdk_xray.types.alias_names

        out["Names"] = aws_sdk_xray.types.alias_names.serialize_json(value["names"])
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Alias:
    out: Alias = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Names" in data:
        import aws_sdk_xray.types.alias_names

        out["names"] = aws_sdk_xray.types.alias_names.deserialize_json(data["Names"])
    if "Type" in data:
        out["type"] = data["Type"]
    return out
