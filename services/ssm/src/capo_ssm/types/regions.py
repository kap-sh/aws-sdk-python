"""Generated from Smithy shape ``com.amazonaws.ssm#Regions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.region

Regions: TypeAlias = list["capo_ssm.types.region.Region"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Regions) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Regions:
    return [item for item in data if item is not None]
