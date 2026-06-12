"""Generated from Smithy shape ``com.amazonaws.imagebuilder#OrganizationArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.organization_arn

OrganizationArnList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.organization_arn.OrganizationArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> OrganizationArnList:
    return list(data)
