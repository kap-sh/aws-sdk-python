"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#Principals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.principal

Principals: TypeAlias = list["capo_global_accelerator.types.principal.Principal"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Principals) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Principals:
    return list(data)
