"""Generated from Smithy shape ``com.amazonaws.batch#KeyValuesPair``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.string_list


class KeyValuesPair(TypedDict):
    name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the filter. Filter names are case sensitive.</p>"""
    values: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    """<p>The filter values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyValuesPair) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "values" in value:
        import aws_sdk_batch.types.string_list

        out["values"] = aws_sdk_batch.types.string_list.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> KeyValuesPair:
    out: KeyValuesPair = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "values" in data:
        import aws_sdk_batch.types.string_list

        out["values"] = aws_sdk_batch.types.string_list.deserialize_json(data["values"])
    return out
