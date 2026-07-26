"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#AdditionalDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.additional_details_key
    import capo_migration_hub_refactor_spaces.types.additional_details_value

AdditionalDetails: TypeAlias = dict[
    "capo_migration_hub_refactor_spaces.types.additional_details_key.AdditionalDetailsKey",
    "capo_migration_hub_refactor_spaces.types.additional_details_value.AdditionalDetailsValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AdditionalDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AdditionalDetails:
    out: AdditionalDetails = {}
    for key, value in data.items():
        out[key] = value
    return out
