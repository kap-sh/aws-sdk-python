"""Generated from Smithy shape ``com.amazonaws.s3tables#NamespaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.namespace_name

NamespaceList: TypeAlias = list["capo_s3tables.types.namespace_name.NamespaceName"]


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceList) -> list:
    return list(value)


def deserialize_json(data: list) -> NamespaceList:
    return list(data)
