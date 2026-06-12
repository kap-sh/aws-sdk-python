"""Generated from Smithy shape ``com.amazonaws.xray#AnomalousServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.anomalous_service

AnomalousServiceList: TypeAlias = list[
    "aws_sdk_xray.types.anomalous_service.AnomalousService"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalousServiceList) -> list:
    import aws_sdk_xray.types.anomalous_service

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.anomalous_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnomalousServiceList:
    import aws_sdk_xray.types.anomalous_service

    out: AnomalousServiceList = []
    for item in data:
        out.append(aws_sdk_xray.types.anomalous_service.deserialize_json(item))
    return out
