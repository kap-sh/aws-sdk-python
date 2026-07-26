"""Generated from Smithy shape ``com.amazonaws.omics#VersionDeleteError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.version_name


class VersionDeleteError(TypedDict, closed=True):
    version_name: "capo_omics.types.version_name.VersionName"
    """<p> The name given to an annotation store version. </p>"""
    message: "str"
    """<p> The message explaining the error in annotation store deletion. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionDeleteError) -> dict:
    out: dict = {}
    out["versionName"] = value["version_name"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> VersionDeleteError:
    out: VersionDeleteError = {}  # type: ignore[typeddict-item]
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    else:
        raise DeserializationError("VersionDeleteError.version_name required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("VersionDeleteError.message required")
    return out
