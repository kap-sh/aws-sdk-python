"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryAssociationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.repository_association_summary

RepositoryAssociationSummaries: TypeAlias = list[
    "aws_sdk_codeguru_reviewer.types.repository_association_summary.RepositoryAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryAssociationSummaries) -> list:
    import aws_sdk_codeguru_reviewer.types.repository_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeguru_reviewer.types.repository_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RepositoryAssociationSummaries:
    import aws_sdk_codeguru_reviewer.types.repository_association_summary

    out: RepositoryAssociationSummaries = []
    for item in data:
        out.append(
            aws_sdk_codeguru_reviewer.types.repository_association_summary.deserialize_json(
                item
            )
        )
    return out
