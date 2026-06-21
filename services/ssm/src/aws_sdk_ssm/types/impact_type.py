"""Generated from Smithy shape ``com.amazonaws.ssm#ImpactType``."""

from typing import Literal, TypeAlias, cast

ImpactType: TypeAlias = Literal[
    "Mutating",
    "NonMutating",
    "Undetermined",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImpactType:
    return cast(ImpactType, data)
