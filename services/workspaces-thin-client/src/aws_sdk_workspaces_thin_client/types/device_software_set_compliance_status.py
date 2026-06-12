"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DeviceSoftwareSetComplianceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

DeviceSoftwareSetComplianceStatus: TypeAlias = Literal[
    "NONE",
    "COMPLIANT",
    "NOT_COMPLIANT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "COMPLIANT",
        "NOT_COMPLIANT",
    )
)


def serialize_json(value: DeviceSoftwareSetComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> DeviceSoftwareSetComplianceStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeviceSoftwareSetComplianceStatus value: {data!r}"
        )
    return cast(DeviceSoftwareSetComplianceStatus, data)
