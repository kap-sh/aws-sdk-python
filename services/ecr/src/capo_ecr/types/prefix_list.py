"""Generated from Smithy shape ``com.amazonaws.ecr#PrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.prefix

PrefixList: TypeAlias = list["capo_ecr.types.prefix.Prefix"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrefixList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PrefixList:
    return list(data)
