"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#JobError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.job_error_code


class JobError(TypedDict, closed=True):
    code: "capo_accessanalyzer.types.job_error_code.JobErrorCode"
    """<p>The job error code.</p>"""
    message: "str"
    """<p>Specific information about the error. For example, which service quota was exceeded or which resource was not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobError) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> JobError:
    out: JobError = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("JobError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("JobError.message required")
    return out
