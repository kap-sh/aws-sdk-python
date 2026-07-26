"""Generated from Smithy shape ``com.amazonaws.transfer#AgreementStatusType``."""

from typing import Literal, TypeAlias, cast

AgreementStatusType: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgreementStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgreementStatusType:
    return cast(AgreementStatusType, data)
