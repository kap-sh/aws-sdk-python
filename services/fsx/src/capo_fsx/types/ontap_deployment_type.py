"""Generated from Smithy shape ``com.amazonaws.fsx#OntapDeploymentType``."""

from typing import Literal, TypeAlias, cast

OntapDeploymentType: TypeAlias = Literal[
    "MULTI_AZ_1",
    "SINGLE_AZ_1",
    "SINGLE_AZ_2",
    "MULTI_AZ_2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OntapDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OntapDeploymentType:
    return cast(OntapDeploymentType, data)
