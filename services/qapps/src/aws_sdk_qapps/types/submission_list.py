"""Generated from Smithy shape ``com.amazonaws.qapps#SubmissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qapps.types.submission

SubmissionList: TypeAlias = list["aws_sdk_qapps.types.submission.Submission"]


# --- restJson1 ser/de ---
def serialize_json(value: SubmissionList) -> list:
    import aws_sdk_qapps.types.submission

    out: list = []
    for item in value:
        out.append(aws_sdk_qapps.types.submission.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubmissionList:
    import aws_sdk_qapps.types.submission

    out: SubmissionList = []
    for item in data:
        out.append(aws_sdk_qapps.types.submission.deserialize_json(item))
    return out
