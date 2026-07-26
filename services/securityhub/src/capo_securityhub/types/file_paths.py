"""Generated from Smithy shape ``com.amazonaws.securityhub#FilePaths``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class FilePaths(TypedDict, closed=True):
    file_path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Path to the infected or suspicious file on the resource it was detected on. </p> <p>Length Constraints: Minimum of 1 length. Maximum of 128 length.</p>"""
    file_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the infected or suspicious file corresponding to the hash. </p> <p>Length Constraints: Minimum of 1 length. Maximum of 128 length.</p>"""
    resource_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the resource on which the threat was detected. </p> <p>Length Constraints: Minimum of 1 length. Maximum of 128 length.</p>"""
    hash: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The hash value for the infected or suspicious file. </p> <p>Length Constraints: Minimum of 1 length. Maximum of 128 length.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilePaths) -> dict:
    out: dict = {}
    if "file_path" in value:
        out["FilePath"] = value["file_path"]
    if "file_name" in value:
        out["FileName"] = value["file_name"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "hash" in value:
        out["Hash"] = value["hash"]
    return out


def deserialize_json(data: dict) -> FilePaths:
    out: FilePaths = {}  # type: ignore[typeddict-item]
    if "FilePath" in data:
        out["file_path"] = data["FilePath"]
    if "FileName" in data:
        out["file_name"] = data["FileName"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "Hash" in data:
        out["hash"] = data["Hash"]
    return out
