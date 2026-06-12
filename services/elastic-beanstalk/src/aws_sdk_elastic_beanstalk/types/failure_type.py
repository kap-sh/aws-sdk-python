"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#FailureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

FailureType: TypeAlias = Literal[
    "UpdateCancelled",
    "CancellationFailed",
    "RollbackFailed",
    "RollbackSuccessful",
    "InternalFailure",
    "InvalidEnvironmentState",
    "PermissionsError",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UpdateCancelled",
        "CancellationFailed",
        "RollbackFailed",
        "RollbackSuccessful",
        "InternalFailure",
        "InvalidEnvironmentState",
        "PermissionsError",
    )
)


def to_query_text(value: FailureType) -> str:
    return value


def from_query_text(text: str) -> FailureType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FailureType value: {text!r}")
    return cast(FailureType, text)


def serialize_query(
    value: FailureType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> FailureType:
    return from_query_text(el.text or "")
