"""Generated from Smithy shape ``com.amazonaws.grafana#OrganizationalUnitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_grafana.types.organizational_unit

OrganizationalUnitList: TypeAlias = list[
    "aws_sdk_grafana.types.organizational_unit.OrganizationalUnit"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnitList) -> list:
    return list(value)


def deserialize_json(data: list) -> OrganizationalUnitList:
    return list(data)
