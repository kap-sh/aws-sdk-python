"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleDmarcPolicy``."""

from typing import Literal, TypeAlias, cast

RuleDmarcPolicy: TypeAlias = Literal[
    "NONE",
    "QUARANTINE",
    "REJECT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleDmarcPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleDmarcPolicy:
    return cast(RuleDmarcPolicy, data)
