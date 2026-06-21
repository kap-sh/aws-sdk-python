"""Generated from Smithy shape ``com.amazonaws.organizations#ResponsibilityTransferType``."""

from typing import Literal, TypeAlias, cast

ResponsibilityTransferType: TypeAlias = Literal["BILLING",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponsibilityTransferType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResponsibilityTransferType:
    return cast(ResponsibilityTransferType, data)
