"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TermsEnforcementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

TermsEnforcementType: TypeAlias = Literal["NONE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NONE",))


def serialize_aws_json_1_1(value: TermsEnforcementType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TermsEnforcementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TermsEnforcementType value: {data!r}")
    return cast(TermsEnforcementType, data)
