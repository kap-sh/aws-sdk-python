"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_summary

DaemonSummariesList: TypeAlias = list["capo_ecs.types.daemon_summary.DaemonSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonSummariesList) -> list:
    import capo_ecs.types.daemon_summary

    out: list = []
    for item in value:
        out.append(capo_ecs.types.daemon_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonSummariesList:
    import capo_ecs.types.daemon_summary

    out: DaemonSummariesList = []
    for item in data:
        out.append(capo_ecs.types.daemon_summary.deserialize_aws_json_1_1(item))
    return out
