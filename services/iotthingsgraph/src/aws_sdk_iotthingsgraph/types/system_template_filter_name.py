"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemTemplateFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

SystemTemplateFilterName: TypeAlias = Literal["FLOW_TEMPLATE_ID",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FLOW_TEMPLATE_ID",))


def serialize_aws_json_1_1(value: SystemTemplateFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SystemTemplateFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SystemTemplateFilterName value: {data!r}")
    return cast(SystemTemplateFilterName, data)
