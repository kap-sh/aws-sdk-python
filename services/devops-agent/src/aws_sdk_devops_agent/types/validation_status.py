"""Generated from Smithy shape ``com.amazonaws.devopsagent#ValidationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Represents the validation state of an association.</p>"""
ValidationStatus: TypeAlias = Literal[
    "valid",
    "invalid",
    "pending-confirmation",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "valid",
        "invalid",
        "pending-confirmation",
    )
)


def serialize_json(value: ValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> ValidationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationStatus value: {data!r}")
    return cast(ValidationStatus, data)
