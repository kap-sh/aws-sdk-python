"""Generated from Smithy shape ``com.amazonaws.route53resolver#ShareStatus``."""

from typing import Literal, TypeAlias, cast

ShareStatus: TypeAlias = Literal[
    "NOT_SHARED",
    "SHARED_WITH_ME",
    "SHARED_BY_ME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShareStatus:
    return cast(ShareStatus, data)
