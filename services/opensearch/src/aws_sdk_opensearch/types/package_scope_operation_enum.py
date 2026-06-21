"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageScopeOperationEnum``."""

from typing import Literal, TypeAlias, cast

PackageScopeOperationEnum: TypeAlias = Literal[
    "ADD",
    "OVERRIDE",
    "REMOVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageScopeOperationEnum) -> str:
    return value


def deserialize_json(data: str) -> PackageScopeOperationEnum:
    return cast(PackageScopeOperationEnum, data)
