"""Generated from Smithy shape ``com.amazonaws.ssmsap#HostList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.host

HostList: TypeAlias = list["aws_sdk_ssm_sap.types.host.Host"]


# --- restJson1 ser/de ---
def serialize_json(value: HostList) -> list:
    import aws_sdk_ssm_sap.types.host

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_sap.types.host.serialize_json(item))
    return out


def deserialize_json(data: list) -> HostList:
    import aws_sdk_ssm_sap.types.host

    out: HostList = []
    for item in data:
        out.append(aws_sdk_ssm_sap.types.host.deserialize_json(item))
    return out
