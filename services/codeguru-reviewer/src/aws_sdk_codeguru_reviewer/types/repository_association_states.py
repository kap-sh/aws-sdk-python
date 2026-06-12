"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryAssociationStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.repository_association_state

RepositoryAssociationStates: TypeAlias = list[
    "aws_sdk_codeguru_reviewer.types.repository_association_state.RepositoryAssociationState"
]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryAssociationStates) -> list:
    import aws_sdk_codeguru_reviewer.types.repository_association_state

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeguru_reviewer.types.repository_association_state.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RepositoryAssociationStates:
    import aws_sdk_codeguru_reviewer.types.repository_association_state

    out: RepositoryAssociationStates = []
    for item in data:
        out.append(
            aws_sdk_codeguru_reviewer.types.repository_association_state.deserialize_json(
                item
            )
        )
    return out
