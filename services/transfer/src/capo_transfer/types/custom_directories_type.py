"""Generated from Smithy shape ``com.amazonaws.transfer#CustomDirectoriesType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.home_directory


class CustomDirectoriesType(TypedDict, closed=True):
    failed_files_directory: "capo_transfer.types.home_directory.HomeDirectory"
    """<p>Specifies a location to store failed AS2 message files.</p>"""
    mdn_files_directory: "capo_transfer.types.home_directory.HomeDirectory"
    """<p>Specifies a location to store MDN files.</p>"""
    payload_files_directory: "capo_transfer.types.home_directory.HomeDirectory"
    """<p>Specifies a location to store the payload for AS2 message files.</p>"""
    status_files_directory: "capo_transfer.types.home_directory.HomeDirectory"
    """<p>Specifies a location to store AS2 status messages.</p>"""
    temporary_files_directory: "capo_transfer.types.home_directory.HomeDirectory"
    """<p>Specifies a location to store temporary AS2 message files.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomDirectoriesType) -> dict:
    out: dict = {}
    out["FailedFilesDirectory"] = value["failed_files_directory"]
    out["MdnFilesDirectory"] = value["mdn_files_directory"]
    out["PayloadFilesDirectory"] = value["payload_files_directory"]
    out["StatusFilesDirectory"] = value["status_files_directory"]
    out["TemporaryFilesDirectory"] = value["temporary_files_directory"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomDirectoriesType:
    out: CustomDirectoriesType = {}  # type: ignore[typeddict-item]
    if "FailedFilesDirectory" in data:
        out["failed_files_directory"] = data["FailedFilesDirectory"]
    else:
        raise DeserializationError(
            "CustomDirectoriesType.failed_files_directory required"
        )
    if "MdnFilesDirectory" in data:
        out["mdn_files_directory"] = data["MdnFilesDirectory"]
    else:
        raise DeserializationError("CustomDirectoriesType.mdn_files_directory required")
    if "PayloadFilesDirectory" in data:
        out["payload_files_directory"] = data["PayloadFilesDirectory"]
    else:
        raise DeserializationError(
            "CustomDirectoriesType.payload_files_directory required"
        )
    if "StatusFilesDirectory" in data:
        out["status_files_directory"] = data["StatusFilesDirectory"]
    else:
        raise DeserializationError(
            "CustomDirectoriesType.status_files_directory required"
        )
    if "TemporaryFilesDirectory" in data:
        out["temporary_files_directory"] = data["TemporaryFilesDirectory"]
    else:
        raise DeserializationError(
            "CustomDirectoriesType.temporary_files_directory required"
        )
    return out
