"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackageIngestState``."""

from typing import Literal, TypeAlias, cast

DatasourcePackageIngestState: TypeAlias = Literal[
    "STARTED",
    "STOPPED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasourcePackageIngestState) -> str:
    return value


def deserialize_json(data: str) -> DatasourcePackageIngestState:
    return cast(DatasourcePackageIngestState, data)
