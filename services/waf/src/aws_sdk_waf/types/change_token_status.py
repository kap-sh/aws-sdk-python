"""Generated from Smithy shape ``com.amazonaws.waf#ChangeTokenStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf.errors import DeserializationError

ChangeTokenStatus: TypeAlias = Literal[
    "PROVISIONED",
    "PENDING",
    "INSYNC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONED",
        "PENDING",
        "INSYNC",
    )
)


def serialize_aws_json_1_1(value: ChangeTokenStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChangeTokenStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeTokenStatus value: {data!r}")
    return cast(ChangeTokenStatus, data)
