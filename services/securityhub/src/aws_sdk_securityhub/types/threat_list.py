"""Generated from Smithy shape ``com.amazonaws.securityhub#ThreatList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.threat

ThreatList: TypeAlias = list["aws_sdk_securityhub.types.threat.Threat"]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatList) -> list:
    import aws_sdk_securityhub.types.threat

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.threat.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatList:
    import aws_sdk_securityhub.types.threat

    out: ThreatList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.threat.deserialize_json(item))
    return out
