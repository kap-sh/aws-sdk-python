"""Generated from Smithy shape ``com.amazonaws.securityhub#AdjustmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.adjustment

AdjustmentList: TypeAlias = list["aws_sdk_securityhub.types.adjustment.Adjustment"]


# --- restJson1 ser/de ---
def serialize_json(value: AdjustmentList) -> list:
    import aws_sdk_securityhub.types.adjustment

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.adjustment.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdjustmentList:
    import aws_sdk_securityhub.types.adjustment

    out: AdjustmentList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.adjustment.deserialize_json(item))
    return out
