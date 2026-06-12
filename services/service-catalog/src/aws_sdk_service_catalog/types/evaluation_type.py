"""Generated from Smithy shape ``com.amazonaws.servicecatalog#EvaluationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

EvaluationType: TypeAlias = Literal[
    "STATIC",
    "DYNAMIC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATIC",
        "DYNAMIC",
    )
)


def serialize_aws_json_1_1(value: EvaluationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EvaluationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationType value: {data!r}")
    return cast(EvaluationType, data)
