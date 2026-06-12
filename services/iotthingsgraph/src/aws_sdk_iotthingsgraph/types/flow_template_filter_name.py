"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowTemplateFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

FlowTemplateFilterName: TypeAlias = Literal["DEVICE_MODEL_ID",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEVICE_MODEL_ID",))


def serialize_aws_json_1_1(value: FlowTemplateFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlowTemplateFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowTemplateFilterName value: {data!r}")
    return cast(FlowTemplateFilterName, data)
