"""Generated from Smithy shape ``com.amazonaws.m2#VsamAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.alternate_key_list
    import aws_sdk_m2.types.boolean
    import aws_sdk_m2.types.primary_key


class VsamAttributes(TypedDict, closed=True):
    format: "str"
    """<p>The record format of the data set.</p>"""
    encoding: NotRequired["str"]
    """<p>The character set used by the data set. Can be ASCII, EBCDIC, or unknown.</p>"""
    compressed: "aws_sdk_m2.types.boolean.Boolean"
    """<p>Indicates whether indexes for this dataset are stored as compressed values. If you have a large data set (typically &gt; 100 Mb), consider setting this flag to True.</p>"""
    primary_key: NotRequired["aws_sdk_m2.types.primary_key.PrimaryKey"]
    """<p>The primary key of the data set.</p>"""
    alternate_keys: NotRequired["aws_sdk_m2.types.alternate_key_list.AlternateKeyList"]
    """<p>The alternate key definitions, if any. A legacy dataset might not have any alternate key defined, but if those alternate keys definitions exist, provide them as some applications will make use of them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VsamAttributes) -> dict:
    out: dict = {}
    out["format"] = value["format"]
    if "encoding" in value:
        out["encoding"] = value["encoding"]
    out["compressed"] = value.get("compressed", False)
    if "primary_key" in value:
        import aws_sdk_m2.types.primary_key

        out["primaryKey"] = aws_sdk_m2.types.primary_key.serialize_json(
            value["primary_key"]
        )
    if "alternate_keys" in value:
        import aws_sdk_m2.types.alternate_key_list

        out["alternateKeys"] = aws_sdk_m2.types.alternate_key_list.serialize_json(
            value["alternate_keys"]
        )
    return out


def deserialize_json(data: dict) -> VsamAttributes:
    out: VsamAttributes = {}  # type: ignore[typeddict-item]
    if "format" in data:
        out["format"] = data["format"]
    else:
        raise DeserializationError("VsamAttributes.format required")
    if "encoding" in data:
        out["encoding"] = data["encoding"]
    if "compressed" in data:
        out["compressed"] = data["compressed"]
    else:
        out["compressed"] = False
    if "primaryKey" in data:
        import aws_sdk_m2.types.primary_key

        out["primary_key"] = aws_sdk_m2.types.primary_key.deserialize_json(
            data["primaryKey"]
        )
    if "alternateKeys" in data:
        import aws_sdk_m2.types.alternate_key_list

        out["alternate_keys"] = aws_sdk_m2.types.alternate_key_list.deserialize_json(
            data["alternateKeys"]
        )
    return out
