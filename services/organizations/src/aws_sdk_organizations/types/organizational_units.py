"""Generated from Smithy shape ``com.amazonaws.organizations#OrganizationalUnits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_organizations.types.organizational_unit

OrganizationalUnits: TypeAlias = list[
    "aws_sdk_organizations.types.organizational_unit.OrganizationalUnit"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationalUnits) -> list:
    import aws_sdk_organizations.types.organizational_unit

    out: list = []
    for item in value:
        out.append(
            aws_sdk_organizations.types.organizational_unit.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationalUnits:
    import aws_sdk_organizations.types.organizational_unit

    out: OrganizationalUnits = []
    for item in data:
        out.append(
            aws_sdk_organizations.types.organizational_unit.deserialize_aws_json_1_1(
                item
            )
        )
    return out
