"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationAlertDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.migration_alert_detail

MigrationAlertDetails: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.migration_alert_detail.MigrationAlertDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationAlertDetails) -> list:
    return list(value)


def deserialize_json(data: list) -> MigrationAlertDetails:
    return list(data)
