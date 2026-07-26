"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchDescribeMergeConflictsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.exception_name
    import capo_codecommit.types.message
    import capo_codecommit.types.path


class BatchDescribeMergeConflictsError(TypedDict, closed=True):
    file_path: "capo_codecommit.types.path.Path"
    """<p>The path to the file.</p>"""
    exception_name: "capo_codecommit.types.exception_name.ExceptionName"
    """<p>The name of the exception.</p>"""
    message: "capo_codecommit.types.message.Message"
    """<p>The message provided by the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDescribeMergeConflictsError) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    out["exceptionName"] = value["exception_name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDescribeMergeConflictsError:
    out: BatchDescribeMergeConflictsError = {}  # type: ignore[typeddict-item]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError(
            "BatchDescribeMergeConflictsError.file_path required"
        )
    if "exceptionName" in data:
        out["exception_name"] = data["exceptionName"]
    else:
        raise DeserializationError(
            "BatchDescribeMergeConflictsError.exception_name required"
        )
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchDescribeMergeConflictsError.message required")
    return out
