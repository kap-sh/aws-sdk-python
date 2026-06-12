"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSecurityFindingIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_security_finding_identifier

AwsSecurityFindingIdentifierList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_security_finding_identifier.AwsSecurityFindingIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsSecurityFindingIdentifierList) -> list:
    import aws_sdk_securityhub.types.aws_security_finding_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_security_finding_identifier.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsSecurityFindingIdentifierList:
    import aws_sdk_securityhub.types.aws_security_finding_identifier

    out: AwsSecurityFindingIdentifierList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_security_finding_identifier.deserialize_json(
                item
            )
        )
    return out
