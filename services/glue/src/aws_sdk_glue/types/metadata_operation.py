"""Generated from Smithy shape ``com.amazonaws.glue#MetadataOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

MetadataOperation: TypeAlias = Literal["CREATE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATE",))


def serialize_aws_json_1_1(value: MetadataOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetadataOperation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetadataOperation value: {data!r}")
    return cast(MetadataOperation, data)
