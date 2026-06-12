"""Generated from Smithy shape ``com.amazonaws.securityhub#CvssList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.cvss

CvssList: TypeAlias = list["aws_sdk_securityhub.types.cvss.Cvss"]


# --- restJson1 ser/de ---
def serialize_json(value: CvssList) -> list:
    import aws_sdk_securityhub.types.cvss

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.cvss.serialize_json(item))
    return out


def deserialize_json(data: list) -> CvssList:
    import aws_sdk_securityhub.types.cvss

    out: CvssList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.cvss.deserialize_json(item))
    return out
