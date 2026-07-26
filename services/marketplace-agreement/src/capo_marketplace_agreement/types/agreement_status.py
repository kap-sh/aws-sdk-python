"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementStatus``."""

from typing import Literal, TypeAlias, cast

AgreementStatus: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
    "CANCELLED",
    "EXPIRED",
    "RENEWED",
    "REPLACED",
    "ROLLED_BACK",
    "SUPERSEDED",
    "TERMINATED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementStatus:
    return cast(AgreementStatus, data)
