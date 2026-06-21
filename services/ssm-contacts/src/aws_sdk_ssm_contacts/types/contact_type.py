"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ContactType``."""

from typing import Literal, TypeAlias, cast

ContactType: TypeAlias = Literal[
    "PERSONAL",
    "ESCALATION",
    "ONCALL_SCHEDULE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContactType:
    return cast(ContactType, data)
