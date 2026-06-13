"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdNamespaceAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_namespace_association_summary

IdNamespaceAssociationSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.id_namespace_association_summary.IdNamespaceAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceAssociationSummaryList) -> list:
    import aws_sdk_cleanrooms.types.id_namespace_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.id_namespace_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdNamespaceAssociationSummaryList:
    import aws_sdk_cleanrooms.types.id_namespace_association_summary

    out: IdNamespaceAssociationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.id_namespace_association_summary.deserialize_json(
                item
            )
        )
    return out
