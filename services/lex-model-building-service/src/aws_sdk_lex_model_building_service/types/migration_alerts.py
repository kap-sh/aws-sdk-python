"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationAlerts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.migration_alert

MigrationAlerts: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.migration_alert.MigrationAlert"
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationAlerts) -> list:
    import aws_sdk_lex_model_building_service.types.migration_alert

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.migration_alert.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MigrationAlerts:
    import aws_sdk_lex_model_building_service.types.migration_alert

    out: MigrationAlerts = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.migration_alert.deserialize_json(
                item
            )
        )
    return out
