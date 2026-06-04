"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonRevisions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_revision

DaemonRevisions: TypeAlias = list["aws_sdk_ecs.types.daemon_revision.DaemonRevision"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonRevisions) -> list:
    import aws_sdk_ecs.types.daemon_revision

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.daemon_revision.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonRevisions:
    import aws_sdk_ecs.types.daemon_revision

    out: DaemonRevisions = []
    for item in data:
        out.append(aws_sdk_ecs.types.daemon_revision.deserialize_aws_json_1_1(item))
    return out
