"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobAbortConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_job_abort_criteria_list


class AwsJobAbortConfig(TypedDict, closed=True):
    abort_criteria_list: (
        "aws_sdk_iot.types.aws_job_abort_criteria_list.AwsJobAbortCriteriaList"
    )
    """<p>The list of criteria that determine when and how to abort the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobAbortConfig) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.aws_job_abort_criteria_list

    out["abortCriteriaList"] = (
        aws_sdk_iot.types.aws_job_abort_criteria_list.serialize_json(
            value["abort_criteria_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> AwsJobAbortConfig:
    out: AwsJobAbortConfig = {}  # type: ignore[typeddict-item]
    if "abortCriteriaList" in data:
        import aws_sdk_iot.types.aws_job_abort_criteria_list

        out["abort_criteria_list"] = (
            aws_sdk_iot.types.aws_job_abort_criteria_list.deserialize_json(
                data["abortCriteriaList"]
            )
        )
    else:
        raise DeserializationError("AwsJobAbortConfig.abort_criteria_list required")
    return out
