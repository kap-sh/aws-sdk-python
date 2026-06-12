"""Generated from Smithy shape ``com.amazonaws.wellarchitected#IssueManagementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

IssueManagementType: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "MANUAL",
    )
)


def serialize_json(value: IssueManagementType) -> str:
    return value


def deserialize_json(data: str) -> IssueManagementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IssueManagementType value: {data!r}")
    return cast(IssueManagementType, data)
