"""Generated from Smithy shape ``com.amazonaws.securityhub#Threat``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.file_path_list
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class Threat(TypedDict):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the threat. </p> <p>Length Constraints: Minimum of 1 length. Maximum of 128 length.</p>"""
    severity: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The severity of the threat. </p> <p>Length Constraints: Minimum of 1 length. Maximum of 128 length.</p>"""
    item_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>This total number of items in which the threat has been detected. </p>"""
    file_paths: NotRequired["aws_sdk_securityhub.types.file_path_list.FilePathList"]
    """<p>Provides information about the file paths that were affected by the threat. </p> <p>Array Members: Minimum number of 1 item. Maximum number of 5 items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Threat) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "severity" in value:
        out["Severity"] = value["severity"]
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "file_paths" in value:
        import aws_sdk_securityhub.types.file_path_list

        out["FilePaths"] = aws_sdk_securityhub.types.file_path_list.serialize_json(
            value["file_paths"]
        )
    return out


def deserialize_json(data: dict) -> Threat:
    out: Threat = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Severity" in data:
        out["severity"] = data["Severity"]
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    if "FilePaths" in data:
        import aws_sdk_securityhub.types.file_path_list

        out["file_paths"] = aws_sdk_securityhub.types.file_path_list.deserialize_json(
            data["FilePaths"]
        )
    return out
