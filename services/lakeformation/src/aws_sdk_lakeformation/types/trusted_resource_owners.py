"""Generated from Smithy shape ``com.amazonaws.lakeformation#TrustedResourceOwners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string

TrustedResourceOwners: TypeAlias = list[
    "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrustedResourceOwners) -> list:
    return list(value)


def deserialize_json(data: list) -> TrustedResourceOwners:
    return list(data)
