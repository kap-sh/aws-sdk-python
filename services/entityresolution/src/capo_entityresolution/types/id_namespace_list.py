"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.id_namespace_summary

IdNamespaceList: TypeAlias = list[
    "capo_entityresolution.types.id_namespace_summary.IdNamespaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceList) -> list:
    import capo_entityresolution.types.id_namespace_summary

    out: list = []
    for item in value:
        out.append(
            capo_entityresolution.types.id_namespace_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IdNamespaceList:
    import capo_entityresolution.types.id_namespace_summary

    out: IdNamespaceList = []
    for item in data:
        out.append(
            capo_entityresolution.types.id_namespace_summary.deserialize_json(item)
        )
    return out
