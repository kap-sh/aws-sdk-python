"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#JobError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.job_error_code


class JobError(TypedDict):
    code: "aws_sdk_accessanalyzer.types.job_error_code.JobErrorCode"
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
