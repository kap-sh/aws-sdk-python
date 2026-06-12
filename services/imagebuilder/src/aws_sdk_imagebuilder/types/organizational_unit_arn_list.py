"""Generated from Smithy shape ``com.amazonaws.imagebuilder#OrganizationalUnitArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.organizational_unit_arn

OrganizationalUnitArnList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.organizational_unit_arn.OrganizationalUnitArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnitArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> OrganizationalUnitArnList:
    return list(data)
