"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressStringEmailAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressStringEmailAttribute: TypeAlias = Literal["RECIPIENT",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("RECIPIENT",))


def serialize_aws_json_1_0(value: IngressStringEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressStringEmailAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IngressStringEmailAttribute value: {data!r}"
        )
    return cast(IngressStringEmailAttribute, data)
