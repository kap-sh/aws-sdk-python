"""Generated from Smithy shape ``com.amazonaws.m2#FileBatchJobDefinition``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError


class FileBatchJobDefinition(TypedDict):
    file_name: "str"
    """<p>The name of the file containing the batch job definition.</p>"""
    folder_path: NotRequired["str"]
    """<p>The path to the file containing the batch job definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileBatchJobDefinition) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    if "folder_path" in value:
        out["folderPath"] = value["folder_path"]
    return out


def deserialize_json(data: dict) -> FileBatchJobDefinition:
    out: FileBatchJobDefinition = {}  # type: ignore[typeddict-item]
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError("FileBatchJobDefinition.file_name required")
    if "folderPath" in data:
        out["folder_path"] = data["folderPath"]
    return out
