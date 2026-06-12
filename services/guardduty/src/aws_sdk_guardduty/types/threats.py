"""Generated from Smithy shape ``com.amazonaws.guardduty#Threats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.threat

Threats: TypeAlias = list["aws_sdk_guardduty.types.threat.Threat"]


# --- restJson1 ser/de ---
def serialize_json(value: Threats) -> list:
    import aws_sdk_guardduty.types.threat

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.threat.serialize_json(item))
    return out


def deserialize_json(data: list) -> Threats:
    import aws_sdk_guardduty.types.threat

    out: Threats = []
    for item in data:
        out.append(aws_sdk_guardduty.types.threat.deserialize_json(item))
    return out
