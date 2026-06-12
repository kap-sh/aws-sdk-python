"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListServerSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.server_summary

ListServerSummary: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.server_summary.ServerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListServerSummary) -> list:
    import aws_sdk_migrationhubstrategy.types.server_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.server_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListServerSummary:
    import aws_sdk_migrationhubstrategy.types.server_summary

    out: ListServerSummary = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.server_summary.deserialize_json(item)
        )
    return out
