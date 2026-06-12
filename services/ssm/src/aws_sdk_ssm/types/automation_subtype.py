"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationSubtype``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AutomationSubtype: TypeAlias = Literal[
    "ChangeRequest",
    "AccessRequest",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ChangeRequest",
        "AccessRequest",
    )
)


def serialize_aws_json_1_1(value: AutomationSubtype) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomationSubtype:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutomationSubtype value: {data!r}")
    return cast(AutomationSubtype, data)
