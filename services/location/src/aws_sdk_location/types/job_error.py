"""Generated from Smithy shape ``com.amazonaws.location#JobError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.job_error_code
    import aws_sdk_location.types.job_error_messages_list


class JobError(TypedDict, closed=True):
    code: "aws_sdk_location.types.job_error_code.JobErrorCode"
    """<p>Error code indicating the type of error that occurred.</p>"""
    messages: NotRequired[
        "aws_sdk_location.types.job_error_messages_list.JobErrorMessagesList"
    ]
    """<p>Error messages providing details about the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobError) -> dict:
    out: dict = {}
    out["Code"] = value["code"]
    if "messages" in value:
        import aws_sdk_location.types.job_error_messages_list

        out["Messages"] = aws_sdk_location.types.job_error_messages_list.serialize_json(
            value["messages"]
        )
    return out


def deserialize_json(data: dict) -> JobError:
    out: JobError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    else:
        raise DeserializationError("JobError.code required")
    if "Messages" in data:
        import aws_sdk_location.types.job_error_messages_list

        out["messages"] = (
            aws_sdk_location.types.job_error_messages_list.deserialize_json(
                data["Messages"]
            )
        )
    return out
