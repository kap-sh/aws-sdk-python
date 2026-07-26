"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TermsSourceType``."""

from typing import Literal, TypeAlias, cast

TermsSourceType: TypeAlias = Literal["LINK",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermsSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TermsSourceType:
    return cast(TermsSourceType, data)
