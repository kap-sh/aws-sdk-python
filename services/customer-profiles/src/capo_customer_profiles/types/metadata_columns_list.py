"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MetadataColumnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.metadata_column_name

MetadataColumnsList: TypeAlias = list[
    "capo_customer_profiles.types.metadata_column_name.MetadataColumnName"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataColumnsList) -> list:
    return list(value)


def deserialize_json(data: list) -> MetadataColumnsList:
    return list(data)
