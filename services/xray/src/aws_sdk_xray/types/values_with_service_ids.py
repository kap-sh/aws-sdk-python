"""Generated from Smithy shape ``com.amazonaws.xray#ValuesWithServiceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.value_with_service_ids

ValuesWithServiceIds: TypeAlias = list[
    "aws_sdk_xray.types.value_with_service_ids.ValueWithServiceIds"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValuesWithServiceIds) -> list:
    import aws_sdk_xray.types.value_with_service_ids

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.value_with_service_ids.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValuesWithServiceIds:
    import aws_sdk_xray.types.value_with_service_ids

    out: ValuesWithServiceIds = []
    for item in data:
        out.append(aws_sdk_xray.types.value_with_service_ids.deserialize_json(item))
    return out
