"""Generated from Smithy shape ``com.amazonaws.ssoadmin#JwksRetrievalOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

JwksRetrievalOption: TypeAlias = Literal["OPEN_ID_DISCOVERY",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OPEN_ID_DISCOVERY",))


def serialize_aws_json_1_1(value: JwksRetrievalOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JwksRetrievalOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JwksRetrievalOption value: {data!r}")
    return cast(JwksRetrievalOption, data)
