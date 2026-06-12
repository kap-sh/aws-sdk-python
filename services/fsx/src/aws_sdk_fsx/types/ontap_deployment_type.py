"""Generated from Smithy shape ``com.amazonaws.fsx#OntapDeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

OntapDeploymentType: TypeAlias = Literal[
    "MULTI_AZ_1",
    "SINGLE_AZ_1",
    "SINGLE_AZ_2",
    "MULTI_AZ_2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MULTI_AZ_1",
        "SINGLE_AZ_1",
        "SINGLE_AZ_2",
        "MULTI_AZ_2",
    )
)


def serialize_aws_json_1_1(value: OntapDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OntapDeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OntapDeploymentType value: {data!r}")
    return cast(OntapDeploymentType, data)
