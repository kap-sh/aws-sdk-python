"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsV2UnprocessedFindingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding

BatchUpdateFindingsV2UnprocessedFindingsList: TypeAlias = list[
    "aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding.BatchUpdateFindingsV2UnprocessedFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsV2UnprocessedFindingsList) -> list:
    import aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateFindingsV2UnprocessedFindingsList:
    import aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding

    out: BatchUpdateFindingsV2UnprocessedFindingsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding.deserialize_json(
                item
            )
        )
    return out
