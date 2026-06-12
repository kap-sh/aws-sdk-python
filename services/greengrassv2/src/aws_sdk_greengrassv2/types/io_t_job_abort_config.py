"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobAbortConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.io_t_job_abort_criteria_list


class IoTJobAbortConfig(TypedDict):
    criteria_list: "aws_sdk_greengrassv2.types.io_t_job_abort_criteria_list.IoTJobAbortCriteriaList"
    """<p>The list of criteria that define when and how to cancel the configuration deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobAbortConfig) -> dict:
    out: dict = {}
    import aws_sdk_greengrassv2.types.io_t_job_abort_criteria_list

    out["criteriaList"] = (
        aws_sdk_greengrassv2.types.io_t_job_abort_criteria_list.serialize_json(
            value["criteria_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> IoTJobAbortConfig:
    out: IoTJobAbortConfig = {}  # type: ignore[typeddict-item]
    if "criteriaList" in data:
        import aws_sdk_greengrassv2.types.io_t_job_abort_criteria_list

        out["criteria_list"] = (
            aws_sdk_greengrassv2.types.io_t_job_abort_criteria_list.deserialize_json(
                data["criteriaList"]
            )
        )
    else:
        raise DeserializationError("IoTJobAbortConfig.criteria_list required")
    return out
