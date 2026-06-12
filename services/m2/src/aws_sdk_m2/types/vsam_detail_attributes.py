"""Generated from Smithy shape ``com.amazonaws.m2#VsamDetailAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_m2.types.alternate_key_list
    import aws_sdk_m2.types.boolean
    import aws_sdk_m2.types.primary_key
    import aws_sdk_m2.types.string20


class VsamDetailAttributes(TypedDict):
    encoding: NotRequired["aws_sdk_m2.types.string20.String20"]
    """<p>The character set used by the data set. Can be ASCII, EBCDIC, or unknown.</p>"""
    record_format: NotRequired["aws_sdk_m2.types.string20.String20"]
    """<p>The record format of the data set.</p>"""
    compressed: NotRequired["aws_sdk_m2.types.boolean.Boolean"]
    """<p>Indicates whether indexes for this dataset are stored as compressed values. If you have a large data set (typically &gt; 100 Mb), consider setting this flag to True.</p>"""
    cache_at_startup: NotRequired["aws_sdk_m2.types.boolean.Boolean"]
    """<p>If set to True, enforces loading the data set into cache before it’s used by the application.</p>"""
    primary_key: NotRequired["aws_sdk_m2.types.primary_key.PrimaryKey"]
    """<p>The primary key of the data set.</p>"""
    alternate_keys: NotRequired["aws_sdk_m2.types.alternate_key_list.AlternateKeyList"]
    """<p>The alternate key definitions, if any. A legacy dataset might not have any alternate key defined, but if those alternate keys definitions exist, provide them as some applications will make use of them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VsamDetailAttributes) -> dict:
    out: dict = {}
    if "encoding" in value:
        out["encoding"] = value["encoding"]
    if "record_format" in value:
        out["recordFormat"] = value["record_format"]
    if "compressed" in value:
        out["compressed"] = value["compressed"]
    if "cache_at_startup" in value:
        out["cacheAtStartup"] = value["cache_at_startup"]
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


def deserialize_json(data: dict) -> VsamDetailAttributes:
    out: VsamDetailAttributes = {}  # type: ignore[typeddict-item]
    if "encoding" in data:
        out["encoding"] = data["encoding"]
    if "recordFormat" in data:
        out["record_format"] = data["recordFormat"]
    if "compressed" in data:
        out["compressed"] = data["compressed"]
    if "cacheAtStartup" in data:
        out["cache_at_startup"] = data["cacheAtStartup"]
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
