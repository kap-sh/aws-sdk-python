"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationAlertReferenceURLs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.migration_alert_reference_url

MigrationAlertReferenceURLs: TypeAlias = list[
    "capo_lex_model_building_service.types.migration_alert_reference_url.MigrationAlertReferenceURL"
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationAlertReferenceURLs) -> list:
    return list(value)


def deserialize_json(data: list) -> MigrationAlertReferenceURLs:
    return list(data)
