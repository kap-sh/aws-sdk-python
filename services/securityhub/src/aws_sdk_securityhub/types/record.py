"""Generated from Smithy shape ``com.amazonaws.securityhub#Record``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.long
    import aws_sdk_securityhub.types.non_empty_string


class Record(TypedDict, closed=True):
    json_path: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path, as a JSONPath expression, to the field in the record that contains the data. If the field name is longer than 20 characters, it is truncated. If the path is longer than 250 characters, it is truncated.</p>"""
    record_index: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>The record index, starting from 0, for the record that contains the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Record) -> dict:
    out: dict = {}
    if "json_path" in value:
        out["JsonPath"] = value["json_path"]
    if "record_index" in value:
        out["RecordIndex"] = value["record_index"]
    return out


def deserialize_json(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if "JsonPath" in data:
        out["json_path"] = data["JsonPath"]
    if "RecordIndex" in data:
        out["record_index"] = data["RecordIndex"]
    return out
