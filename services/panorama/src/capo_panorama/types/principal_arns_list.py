"""Generated from Smithy shape ``com.amazonaws.panorama#PrincipalArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.principal_arn

PrincipalArnsList: TypeAlias = list["capo_panorama.types.principal_arn.PrincipalArn"]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalArnsList) -> list:
    return list(value)


def deserialize_json(data: list) -> PrincipalArnsList:
    return list(data)
