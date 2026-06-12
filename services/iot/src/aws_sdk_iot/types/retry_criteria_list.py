"""Generated from Smithy shape ``com.amazonaws.iot#RetryCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.retry_criteria

RetryCriteriaList: TypeAlias = list["aws_sdk_iot.types.retry_criteria.RetryCriteria"]


# --- restJson1 ser/de ---
def serialize_json(value: RetryCriteriaList) -> list:
    import aws_sdk_iot.types.retry_criteria

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.retry_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> RetryCriteriaList:
    import aws_sdk_iot.types.retry_criteria

    out: RetryCriteriaList = []
    for item in data:
        out.append(aws_sdk_iot.types.retry_criteria.deserialize_json(item))
    return out
