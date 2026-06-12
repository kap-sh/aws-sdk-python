"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceTypeOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

ServiceTypeOption: TypeAlias = Literal["HTTP",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HTTP",))


def serialize_aws_json_1_1(value: ServiceTypeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceTypeOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceTypeOption value: {data!r}")
    return cast(ServiceTypeOption, data)
