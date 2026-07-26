"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSecurityFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_security_finding

AwsSecurityFindingList: TypeAlias = list[
    "capo_securityhub.types.aws_security_finding.AwsSecurityFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsSecurityFindingList) -> list:
    import capo_securityhub.types.aws_security_finding

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.aws_security_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsSecurityFindingList:
    import capo_securityhub.types.aws_security_finding

    out: AwsSecurityFindingList = []
    for item in data:
        out.append(capo_securityhub.types.aws_security_finding.deserialize_json(item))
    return out
