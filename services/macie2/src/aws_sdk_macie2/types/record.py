"""Generated from Smithy shape ``com.amazonaws.macie2#Record``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long
    import aws_sdk_macie2.types.__string


class Record(TypedDict):
    json_path: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The path, as a JSONPath expression, to the sensitive data. For an Avro object container or Parquet file, this is the path to the field in the record (recordIndex) that contains the data. For a JSON or JSON Lines file, this is the path to the field or array that contains the data. If the data is a value in an array, the path also indicates which value contains the data.</p> <p>If Amazon Macie detects sensitive data in the name of any element in the path, Macie omits this field. If the name of an element exceeds 240 characters, Macie truncates the name by removing characters from the beginning of the name. If the resulting full path exceeds 250 characters, Macie also truncates the path, starting with the first element in the path, until the path contains 250 or fewer characters.</p>"""
    record_index: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>For an Avro object container or Parquet file, the record index, starting from 0, for the record that contains the sensitive data. For a JSON Lines file, the line index, starting from 0, for the line that contains the sensitive data. This value is always 0 for JSON files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Record) -> dict:
    out: dict = {}
    if "json_path" in value:
        out["jsonPath"] = value["json_path"]
    if "record_index" in value:
        out["recordIndex"] = value["record_index"]
    return out


def deserialize_json(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if "jsonPath" in data:
        out["json_path"] = data["jsonPath"]
    if "recordIndex" in data:
        out["record_index"] = data["recordIndex"]
    return out
