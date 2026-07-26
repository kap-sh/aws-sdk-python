"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonRevisionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_revision_detail

DaemonRevisionDetailList: TypeAlias = list[
    "capo_ecs.types.daemon_revision_detail.DaemonRevisionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonRevisionDetailList) -> list:
    import capo_ecs.types.daemon_revision_detail

    out: list = []
    for item in value:
        out.append(capo_ecs.types.daemon_revision_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonRevisionDetailList:
    import capo_ecs.types.daemon_revision_detail

    out: DaemonRevisionDetailList = []
    for item in data:
        out.append(capo_ecs.types.daemon_revision_detail.deserialize_aws_json_1_1(item))
    return out
