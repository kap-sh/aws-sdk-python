"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackage``."""

from typing import Literal, TypeAlias, cast

DatasourcePackage: TypeAlias = Literal[
    "DETECTIVE_CORE",
    "EKS_AUDIT",
    "ASFF_SECURITYHUB_FINDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasourcePackage) -> str:
    return value


def deserialize_json(data: str) -> DatasourcePackage:
    return cast(DatasourcePackage, data)
