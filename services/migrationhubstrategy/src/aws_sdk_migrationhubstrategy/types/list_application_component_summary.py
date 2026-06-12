"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListApplicationComponentSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.application_component_summary

ListApplicationComponentSummary: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.application_component_summary.ApplicationComponentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationComponentSummary) -> list:
    import aws_sdk_migrationhubstrategy.types.application_component_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.application_component_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListApplicationComponentSummary:
    import aws_sdk_migrationhubstrategy.types.application_component_summary

    out: ListApplicationComponentSummary = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.application_component_summary.deserialize_json(
                item
            )
        )
    return out
