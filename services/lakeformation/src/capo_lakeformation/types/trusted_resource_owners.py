"""Generated from Smithy shape ``com.amazonaws.lakeformation#TrustedResourceOwners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string

TrustedResourceOwners: TypeAlias = list[
    "capo_lakeformation.types.catalog_id_string.CatalogIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrustedResourceOwners) -> list:
    return list(value)


def deserialize_json(data: list) -> TrustedResourceOwners:
    return list(data)
