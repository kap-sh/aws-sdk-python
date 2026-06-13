"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorTopContributorsRowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.monitor_top_contributors_row

MonitorTopContributorsRowList: TypeAlias = list[
    "aws_sdk_networkflowmonitor.types.monitor_top_contributors_row.MonitorTopContributorsRow"
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorTopContributorsRowList) -> list:
    import aws_sdk_networkflowmonitor.types.monitor_top_contributors_row

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkflowmonitor.types.monitor_top_contributors_row.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MonitorTopContributorsRowList:
    import aws_sdk_networkflowmonitor.types.monitor_top_contributors_row

    out: MonitorTopContributorsRowList = []
    for item in data:
        out.append(
            aws_sdk_networkflowmonitor.types.monitor_top_contributors_row.deserialize_json(
                item
            )
        )
    return out
