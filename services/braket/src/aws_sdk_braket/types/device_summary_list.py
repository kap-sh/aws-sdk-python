"""Generated from Smithy shape ``com.amazonaws.braket#DeviceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_braket.types.device_summary

DeviceSummaryList: TypeAlias = list["aws_sdk_braket.types.device_summary.DeviceSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceSummaryList) -> list:
    import aws_sdk_braket.types.device_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_braket.types.device_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceSummaryList:
    import aws_sdk_braket.types.device_summary
    out: DeviceSummaryList = []
    for item in data:
        out.append(aws_sdk_braket.types.device_summary.deserialize_json(item))
    return out