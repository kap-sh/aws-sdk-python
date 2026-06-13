"""Generated from Smithy shape ``com.amazonaws.qconnect#RuntimeSessionDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.runtime_session_data

RuntimeSessionDataList: TypeAlias = list[
    "aws_sdk_qconnect.types.runtime_session_data.RuntimeSessionData"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeSessionDataList) -> list:
    import aws_sdk_qconnect.types.runtime_session_data

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.runtime_session_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuntimeSessionDataList:
    import aws_sdk_qconnect.types.runtime_session_data

    out: RuntimeSessionDataList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.runtime_session_data.deserialize_json(item))
    return out
