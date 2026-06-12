"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationSyncCompliance``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AssociationSyncCompliance: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "MANUAL",
    )
)


def serialize_aws_json_1_1(value: AssociationSyncCompliance) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationSyncCompliance:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationSyncCompliance value: {data!r}")
    return cast(AssociationSyncCompliance, data)
