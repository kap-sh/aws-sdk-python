"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssociationEdgeType``."""

from typing import Literal, TypeAlias, cast

AssociationEdgeType: TypeAlias = Literal[
    "ContributedTo",
    "AssociatedWith",
    "DerivedFrom",
    "Produced",
    "SameAs",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationEdgeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationEdgeType:
    return cast(AssociationEdgeType, data)
