"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsUnprocessedFindingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.batch_update_findings_unprocessed_finding

BatchUpdateFindingsUnprocessedFindingsList: TypeAlias = list[
    "aws_sdk_securityhub.types.batch_update_findings_unprocessed_finding.BatchUpdateFindingsUnprocessedFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsUnprocessedFindingsList) -> list:
    import aws_sdk_securityhub.types.batch_update_findings_unprocessed_finding

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.batch_update_findings_unprocessed_finding.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateFindingsUnprocessedFindingsList:
    import aws_sdk_securityhub.types.batch_update_findings_unprocessed_finding

    out: BatchUpdateFindingsUnprocessedFindingsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.batch_update_findings_unprocessed_finding.deserialize_json(
                item
            )
        )
    return out
