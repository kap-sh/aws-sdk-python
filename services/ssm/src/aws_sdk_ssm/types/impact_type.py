"""Generated from Smithy shape ``com.amazonaws.ssm#ImpactType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ImpactType: TypeAlias = Literal[
    "Mutating",
    "NonMutating",
    "Undetermined",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Mutating",
        "NonMutating",
        "Undetermined",
    )
)


def serialize_aws_json_1_1(value: ImpactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImpactType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImpactType value: {data!r}")
    return cast(ImpactType, data)
