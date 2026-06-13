"""Generated from Smithy shape ``com.amazonaws.s3tables#NamespaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.namespace_name

NamespaceList: TypeAlias = list["aws_sdk_s3tables.types.namespace_name.NamespaceName"]


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceList) -> list:
    return list(value)


def deserialize_json(data: list) -> NamespaceList:
    return list(data)
