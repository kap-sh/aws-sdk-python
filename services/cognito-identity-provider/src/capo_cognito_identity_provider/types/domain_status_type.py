"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DomainStatusType``."""

from typing import Literal, TypeAlias, cast

DomainStatusType: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "UPDATING",
    "ACTIVE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainStatusType:
    return cast(DomainStatusType, data)
