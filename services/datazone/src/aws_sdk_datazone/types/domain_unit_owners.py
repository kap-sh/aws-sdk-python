"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitOwners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_unit_owner_properties

DomainUnitOwners: TypeAlias = list[
    "aws_sdk_datazone.types.domain_unit_owner_properties.DomainUnitOwnerProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitOwners) -> list:
    import aws_sdk_datazone.types.domain_unit_owner_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.domain_unit_owner_properties.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DomainUnitOwners:
    import aws_sdk_datazone.types.domain_unit_owner_properties

    out: DomainUnitOwners = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.domain_unit_owner_properties.deserialize_json(item)
        )
    return out
