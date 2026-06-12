"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackageIngestState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

DatasourcePackageIngestState: TypeAlias = Literal[
    "STARTED",
    "STOPPED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTED",
        "STOPPED",
        "DISABLED",
    )
)


def serialize_json(value: DatasourcePackageIngestState) -> str:
    return value


def deserialize_json(data: str) -> DatasourcePackageIngestState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DatasourcePackageIngestState value: {data!r}"
        )
    return cast(DatasourcePackageIngestState, data)
