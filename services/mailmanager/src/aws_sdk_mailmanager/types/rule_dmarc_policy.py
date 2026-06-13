"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleDmarcPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleDmarcPolicy: TypeAlias = Literal[
    "NONE",
    "QUARANTINE",
    "REJECT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "QUARANTINE",
        "REJECT",
    )
)


def serialize_aws_json_1_0(value: RuleDmarcPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleDmarcPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleDmarcPolicy value: {data!r}")
    return cast(RuleDmarcPolicy, data)
