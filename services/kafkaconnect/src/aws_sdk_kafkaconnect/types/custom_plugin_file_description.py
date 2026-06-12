"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CustomPluginFileDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__long
    import aws_sdk_kafkaconnect.types.__string


class CustomPluginFileDescription(TypedDict):
    file_md5: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The hex-encoded MD5 checksum of the custom plugin file. You can use it to validate the file.</p>"""
    file_size: "aws_sdk_kafkaconnect.types.__long.__long"
    """<p>The size in bytes of the custom plugin file. You can use it to validate the file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPluginFileDescription) -> dict:
    out: dict = {}
    if "file_md5" in value:
        out["fileMd5"] = value["file_md5"]
    out["fileSize"] = value.get("file_size", 0)
    return out


def deserialize_json(data: dict) -> CustomPluginFileDescription:
    out: CustomPluginFileDescription = {}  # type: ignore[typeddict-item]
    if "fileMd5" in data:
        out["file_md5"] = data["fileMd5"]
    if "fileSize" in data:
        out["file_size"] = data["fileSize"]
    else:
        out["file_size"] = 0
    return out
