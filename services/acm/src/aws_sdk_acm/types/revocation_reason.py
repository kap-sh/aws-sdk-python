"""Generated from Smithy shape ``com.amazonaws.acm#RevocationReason``."""

from typing import Literal, TypeAlias, cast

RevocationReason: TypeAlias = Literal[
    "UNSPECIFIED",
    "KEY_COMPROMISE",
    "CA_COMPROMISE",
    "AFFILIATION_CHANGED",
    "SUPERCEDED",
    "SUPERSEDED",
    "CESSATION_OF_OPERATION",
    "CERTIFICATE_HOLD",
    "REMOVE_FROM_CRL",
    "PRIVILEGE_WITHDRAWN",
    "A_A_COMPROMISE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevocationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RevocationReason:
    return cast(RevocationReason, data)
