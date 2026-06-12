"""Generated from Smithy shape ``com.amazonaws.iot#AbortCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.abort_criteria

AbortCriteriaList: TypeAlias = list["aws_sdk_iot.types.abort_criteria.AbortCriteria"]


# --- restJson1 ser/de ---
def serialize_json(value: AbortCriteriaList) -> list:
    import aws_sdk_iot.types.abort_criteria

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.abort_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> AbortCriteriaList:
    import aws_sdk_iot.types.abort_criteria

    out: AbortCriteriaList = []
    for item in data:
        out.append(aws_sdk_iot.types.abort_criteria.deserialize_json(item))
    return out
