"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchImportFindingsRequestFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_security_finding

BatchImportFindingsRequestFindingList: TypeAlias = list[
    "capo_securityhub.types.aws_security_finding.AwsSecurityFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportFindingsRequestFindingList) -> list:
    import capo_securityhub.types.aws_security_finding

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.aws_security_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchImportFindingsRequestFindingList:
    import capo_securityhub.types.aws_security_finding

    out: BatchImportFindingsRequestFindingList = []
    for item in data:
        out.append(capo_securityhub.types.aws_security_finding.deserialize_json(item))
    return out
