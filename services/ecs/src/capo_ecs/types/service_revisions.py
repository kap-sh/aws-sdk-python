"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_revision

ServiceRevisions: TypeAlias = list["capo_ecs.types.service_revision.ServiceRevision"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRevisions) -> list:
    import capo_ecs.types.service_revision

    out: list = []
    for item in value:
        out.append(capo_ecs.types.service_revision.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceRevisions:
    import capo_ecs.types.service_revision

    out: ServiceRevisions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.service_revision.deserialize_aws_json_1_1(item))
    return out
