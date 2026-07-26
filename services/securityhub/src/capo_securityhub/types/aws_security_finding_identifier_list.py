"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSecurityFindingIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_security_finding_identifier

AwsSecurityFindingIdentifierList: TypeAlias = list[
    "capo_securityhub.types.aws_security_finding_identifier.AwsSecurityFindingIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsSecurityFindingIdentifierList) -> list:
    import capo_securityhub.types.aws_security_finding_identifier

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_security_finding_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsSecurityFindingIdentifierList:
    import capo_securityhub.types.aws_security_finding_identifier

    out: AwsSecurityFindingIdentifierList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_security_finding_identifier.deserialize_json(
                item
            )
        )
    return out
