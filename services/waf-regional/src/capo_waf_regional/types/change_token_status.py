"""Generated from Smithy shape ``com.amazonaws.wafregional#ChangeTokenStatus``."""

from typing import Literal, TypeAlias, cast

ChangeTokenStatus: TypeAlias = Literal[
    "PROVISIONED",
    "PENDING",
    "INSYNC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChangeTokenStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChangeTokenStatus:
    return cast(ChangeTokenStatus, data)
