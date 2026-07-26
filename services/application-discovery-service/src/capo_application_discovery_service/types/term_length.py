"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#TermLength``."""

from typing import Literal, TypeAlias, cast

TermLength: TypeAlias = Literal[
    "ONE_YEAR",
    "THREE_YEAR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermLength) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TermLength:
    return cast(TermLength, data)
