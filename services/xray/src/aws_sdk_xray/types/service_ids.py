"""Generated from Smithy shape ``com.amazonaws.xray#ServiceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.service_id

ServiceIds: TypeAlias = list["aws_sdk_xray.types.service_id.ServiceId"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceIds) -> list:
    import aws_sdk_xray.types.service_id

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.service_id.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceIds:
    import aws_sdk_xray.types.service_id

    out: ServiceIds = []
    for item in data:
        out.append(aws_sdk_xray.types.service_id.deserialize_json(item))
    return out
