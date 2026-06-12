"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.finding_id

FindingIdList: TypeAlias = list["aws_sdk_accessanalyzer.types.finding_id.FindingId"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> FindingIdList:
    return list(data)
