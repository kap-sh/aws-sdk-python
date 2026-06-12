"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsV2ProcessedFindingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.batch_update_findings_v2_processed_finding

BatchUpdateFindingsV2ProcessedFindingsList: TypeAlias = list[
    "aws_sdk_securityhub.types.batch_update_findings_v2_processed_finding.BatchUpdateFindingsV2ProcessedFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsV2ProcessedFindingsList) -> list:
    import aws_sdk_securityhub.types.batch_update_findings_v2_processed_finding

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.batch_update_findings_v2_processed_finding.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateFindingsV2ProcessedFindingsList:
    import aws_sdk_securityhub.types.batch_update_findings_v2_processed_finding

    out: BatchUpdateFindingsV2ProcessedFindingsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.batch_update_findings_v2_processed_finding.deserialize_json(
                item
            )
        )
    return out
