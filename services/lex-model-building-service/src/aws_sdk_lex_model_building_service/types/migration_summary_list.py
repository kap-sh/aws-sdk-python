"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.migration_summary

MigrationSummaryList: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.migration_summary.MigrationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationSummaryList) -> list:
    import aws_sdk_lex_model_building_service.types.migration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.migration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MigrationSummaryList:
    import aws_sdk_lex_model_building_service.types.migration_summary

    out: MigrationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.migration_summary.deserialize_json(
                item
            )
        )
    return out
