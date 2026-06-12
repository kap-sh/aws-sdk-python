"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#RouteSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.route_summary

RouteSummaries: TypeAlias = list[
    "aws_sdk_migration_hub_refactor_spaces.types.route_summary.RouteSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSummaries) -> list:
    import aws_sdk_migration_hub_refactor_spaces.types.route_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migration_hub_refactor_spaces.types.route_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteSummaries:
    import aws_sdk_migration_hub_refactor_spaces.types.route_summary

    out: RouteSummaries = []
    for item in data:
        out.append(
            aws_sdk_migration_hub_refactor_spaces.types.route_summary.deserialize_json(
                item
            )
        )
    return out
