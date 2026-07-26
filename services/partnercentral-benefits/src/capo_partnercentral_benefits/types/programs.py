"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Programs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.program

Programs: TypeAlias = list["capo_partnercentral_benefits.types.program.Program"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Programs) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Programs:
    return list(data)
