"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#EnvironmentSoftwareSetComplianceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

EnvironmentSoftwareSetComplianceStatus: TypeAlias = Literal[
    "NO_REGISTERED_DEVICES",
    "COMPLIANT",
    "NOT_COMPLIANT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_REGISTERED_DEVICES",
        "COMPLIANT",
        "NOT_COMPLIANT",
    )
)


def serialize_json(value: EnvironmentSoftwareSetComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> EnvironmentSoftwareSetComplianceStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EnvironmentSoftwareSetComplianceStatus value: {data!r}"
        )
    return cast(EnvironmentSoftwareSetComplianceStatus, data)
