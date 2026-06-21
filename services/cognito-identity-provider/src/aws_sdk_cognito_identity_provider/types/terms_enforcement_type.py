"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TermsEnforcementType``."""

from typing import Literal, TypeAlias, cast

TermsEnforcementType: TypeAlias = Literal["NONE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermsEnforcementType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TermsEnforcementType:
    return cast(TermsEnforcementType, data)
