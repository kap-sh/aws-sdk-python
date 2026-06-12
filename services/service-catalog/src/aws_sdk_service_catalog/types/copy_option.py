"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CopyOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

CopyOption: TypeAlias = Literal["CopyTags",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CopyTags",))


def serialize_aws_json_1_1(value: CopyOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CopyOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CopyOption value: {data!r}")
    return cast(CopyOption, data)
