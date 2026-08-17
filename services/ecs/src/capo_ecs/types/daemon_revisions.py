"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonRevisions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_revision

DaemonRevisions: TypeAlias = list["capo_ecs.types.daemon_revision.DaemonRevision"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonRevisions) -> list:
    import capo_ecs.types.daemon_revision

    out: list = []
    for item in value:
        out.append(capo_ecs.types.daemon_revision.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonRevisions:
    import capo_ecs.types.daemon_revision

    out: DaemonRevisions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.daemon_revision.deserialize_aws_json_1_1(item))
    return out
