"""Generated from Smithy shape ``com.amazonaws.organizations#ResponsibilityTransferStatus``."""

from typing import Literal, TypeAlias, cast

ResponsibilityTransferStatus: TypeAlias = Literal[
    "REQUESTED",
    "DECLINED",
    "CANCELED",
    "EXPIRED",
    "ACCEPTED",
    "WITHDRAWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponsibilityTransferStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResponsibilityTransferStatus:
    return cast(ResponsibilityTransferStatus, data)
