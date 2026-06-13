"""Generated from Smithy shape ``com.amazonaws.inspector2#FindingArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.finding_arn

FindingArnList: TypeAlias = list["aws_sdk_inspector2.types.finding_arn.FindingArn"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> FindingArnList:
    return list(data)
