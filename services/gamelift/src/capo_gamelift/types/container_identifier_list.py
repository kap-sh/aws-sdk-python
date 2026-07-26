"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_identifier

ContainerIdentifierList: TypeAlias = list[
    "capo_gamelift.types.container_identifier.ContainerIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerIdentifierList) -> list:
    import capo_gamelift.types.container_identifier

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_identifier.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerIdentifierList:
    import capo_gamelift.types.container_identifier

    out: ContainerIdentifierList = []
    for item in data:
        out.append(
            capo_gamelift.types.container_identifier.deserialize_aws_json_1_1(item)
        )
    return out
