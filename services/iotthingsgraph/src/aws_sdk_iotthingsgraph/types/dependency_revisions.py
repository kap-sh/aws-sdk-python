"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DependencyRevisions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.dependency_revision

DependencyRevisions: TypeAlias = list[
    "aws_sdk_iotthingsgraph.types.dependency_revision.DependencyRevision"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependencyRevisions) -> list:
    import aws_sdk_iotthingsgraph.types.dependency_revision

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotthingsgraph.types.dependency_revision.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DependencyRevisions:
    import aws_sdk_iotthingsgraph.types.dependency_revision

    out: DependencyRevisions = []
    for item in data:
        out.append(
            aws_sdk_iotthingsgraph.types.dependency_revision.deserialize_aws_json_1_1(
                item
            )
        )
    return out
