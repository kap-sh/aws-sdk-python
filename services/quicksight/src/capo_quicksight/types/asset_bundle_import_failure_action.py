"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportFailureAction``."""

from typing import Literal, TypeAlias, cast

AssetBundleImportFailureAction: TypeAlias = Literal[
    "DO_NOTHING",
    "ROLLBACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportFailureAction) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleImportFailureAction:
    return cast(AssetBundleImportFailureAction, data)
