"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportFailureAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleImportFailureAction: TypeAlias = Literal[
    "DO_NOTHING",
    "ROLLBACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DO_NOTHING",
        "ROLLBACK",
    )
)


def serialize_json(value: AssetBundleImportFailureAction) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleImportFailureAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleImportFailureAction value: {data!r}"
        )
    return cast(AssetBundleImportFailureAction, data)
