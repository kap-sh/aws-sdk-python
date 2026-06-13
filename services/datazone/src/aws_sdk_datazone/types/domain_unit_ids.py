"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_unit_id

DomainUnitIds: TypeAlias = list["aws_sdk_datazone.types.domain_unit_id.DomainUnitId"]


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitIds) -> list:
    return list(value)


def deserialize_json(data: list) -> DomainUnitIds:
    return list(data)
