"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdict``."""

from typing import Literal, TypeAlias, cast

RuleVerdict: TypeAlias = Literal[
    "PASS",
    "FAIL",
    "GRAY",
    "PROCESSING_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVerdict) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleVerdict:
    return cast(RuleVerdict, data)
