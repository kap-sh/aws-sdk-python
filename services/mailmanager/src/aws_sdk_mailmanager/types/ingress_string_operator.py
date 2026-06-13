"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressStringOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressStringOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOT_EQUALS",
        "STARTS_WITH",
        "ENDS_WITH",
        "CONTAINS",
    )
)


def serialize_aws_json_1_0(value: IngressStringOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressStringOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngressStringOperator value: {data!r}")
    return cast(IngressStringOperator, data)
