"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionsRetryConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.retry_criteria_list


class JobExecutionsRetryConfig(TypedDict):
    criteria_list: "aws_sdk_iot.types.retry_criteria_list.RetryCriteriaList"
    """<p>The list of criteria that determines how many retries are allowed for each failure type for a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionsRetryConfig) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.retry_criteria_list

    out["criteriaList"] = aws_sdk_iot.types.retry_criteria_list.serialize_json(
        value["criteria_list"]
    )
    return out


def deserialize_json(data: dict) -> JobExecutionsRetryConfig:
    out: JobExecutionsRetryConfig = {}  # type: ignore[typeddict-item]
    if "criteriaList" in data:
        import aws_sdk_iot.types.retry_criteria_list

        out["criteria_list"] = aws_sdk_iot.types.retry_criteria_list.deserialize_json(
            data["criteriaList"]
        )
    else:
        raise DeserializationError("JobExecutionsRetryConfig.criteria_list required")
    return out
