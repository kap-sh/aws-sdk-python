"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfFindingIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.ocsf_finding_identifier

OcsfFindingIdentifierList: TypeAlias = list[
    "aws_sdk_securityhub.types.ocsf_finding_identifier.OcsfFindingIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfFindingIdentifierList) -> list:
    import aws_sdk_securityhub.types.ocsf_finding_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.ocsf_finding_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OcsfFindingIdentifierList:
    import aws_sdk_securityhub.types.ocsf_finding_identifier

    out: OcsfFindingIdentifierList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.ocsf_finding_identifier.deserialize_json(item)
        )
    return out
