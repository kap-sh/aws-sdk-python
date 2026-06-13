"""Generated from Smithy shape ``com.amazonaws.securityagent#RiskTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.risk_type

RiskTypeList: TypeAlias = list["aws_sdk_securityagent.types.risk_type.RiskType"]


# --- restJson1 ser/de ---
def serialize_json(value: RiskTypeList) -> list:
    import aws_sdk_securityagent.types.risk_type

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.risk_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> RiskTypeList:
    import aws_sdk_securityagent.types.risk_type

    out: RiskTypeList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.risk_type.deserialize_json(item))
    return out
