"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssociationEdgeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AssociationEdgeType: TypeAlias = Literal[
    "ContributedTo",
    "AssociatedWith",
    "DerivedFrom",
    "Produced",
    "SameAs",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ContributedTo",
        "AssociatedWith",
        "DerivedFrom",
        "Produced",
        "SameAs",
    )
)


def serialize_aws_json_1_1(value: AssociationEdgeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationEdgeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationEdgeType value: {data!r}")
    return cast(AssociationEdgeType, data)
