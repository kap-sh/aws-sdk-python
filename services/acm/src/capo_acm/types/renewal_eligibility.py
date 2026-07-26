"""Generated from Smithy shape ``com.amazonaws.acm#RenewalEligibility``."""

from typing import Literal, TypeAlias, cast

RenewalEligibility: TypeAlias = Literal[
    "ELIGIBLE",
    "INELIGIBLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewalEligibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RenewalEligibility:
    return cast(RenewalEligibility, data)
