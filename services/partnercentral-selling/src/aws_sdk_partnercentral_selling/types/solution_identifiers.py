"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SolutionIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.solution_identifier

SolutionIdentifiers: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.solution_identifier.SolutionIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SolutionIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SolutionIdentifiers:
    return list(data)
