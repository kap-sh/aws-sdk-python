"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TermsSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

TermsSourceType: TypeAlias = Literal["LINK",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LINK",))


def serialize_aws_json_1_1(value: TermsSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TermsSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TermsSourceType value: {data!r}")
    return cast(TermsSourceType, data)
