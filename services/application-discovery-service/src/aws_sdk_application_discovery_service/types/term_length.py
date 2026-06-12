"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#TermLength``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

TermLength: TypeAlias = Literal[
    "ONE_YEAR",
    "THREE_YEAR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_YEAR",
        "THREE_YEAR",
    )
)


def serialize_aws_json_1_1(value: TermLength) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TermLength:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TermLength value: {data!r}")
    return cast(TermLength, data)
