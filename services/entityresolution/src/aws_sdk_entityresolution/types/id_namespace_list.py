"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_namespace_summary

IdNamespaceList: TypeAlias = list[
    "aws_sdk_entityresolution.types.id_namespace_summary.IdNamespaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceList) -> list:
    import aws_sdk_entityresolution.types.id_namespace_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.id_namespace_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IdNamespaceList:
    import aws_sdk_entityresolution.types.id_namespace_summary

    out: IdNamespaceList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.id_namespace_summary.deserialize_json(item)
        )
    return out
