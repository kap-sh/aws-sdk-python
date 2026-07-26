"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationSubtype``."""

from typing import Literal, TypeAlias, cast

AutomationSubtype: TypeAlias = Literal[
    "ChangeRequest",
    "AccessRequest",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationSubtype) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomationSubtype:
    return cast(AutomationSubtype, data)
