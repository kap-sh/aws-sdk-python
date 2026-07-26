"""Generated from Smithy shape ``com.amazonaws.securityhub#CvssList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.cvss

CvssList: TypeAlias = list["capo_securityhub.types.cvss.Cvss"]


# --- restJson1 ser/de ---
def serialize_json(value: CvssList) -> list:
    import capo_securityhub.types.cvss

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.cvss.serialize_json(item))
    return out


def deserialize_json(data: list) -> CvssList:
    import capo_securityhub.types.cvss

    out: CvssList = []
    for item in data:
        out.append(capo_securityhub.types.cvss.deserialize_json(item))
    return out
