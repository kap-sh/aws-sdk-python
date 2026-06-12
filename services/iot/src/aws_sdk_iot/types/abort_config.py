"""Generated from Smithy shape ``com.amazonaws.iot#AbortConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.abort_criteria_list


class AbortConfig(TypedDict):
    criteria_list: "aws_sdk_iot.types.abort_criteria_list.AbortCriteriaList"
    """<p>The list of criteria that determine when and how to abort the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AbortConfig) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.abort_criteria_list

    out["criteriaList"] = aws_sdk_iot.types.abort_criteria_list.serialize_json(
        value["criteria_list"]
    )
    return out


def deserialize_json(data: dict) -> AbortConfig:
    out: AbortConfig = {}  # type: ignore[typeddict-item]
    if "criteriaList" in data:
        import aws_sdk_iot.types.abort_criteria_list

        out["criteria_list"] = aws_sdk_iot.types.abort_criteria_list.deserialize_json(
            data["criteriaList"]
        )
    else:
        raise DeserializationError("AbortConfig.criteria_list required")
    return out
