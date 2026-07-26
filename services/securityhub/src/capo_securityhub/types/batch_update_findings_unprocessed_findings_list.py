"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsUnprocessedFindingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.batch_update_findings_unprocessed_finding

BatchUpdateFindingsUnprocessedFindingsList: TypeAlias = list[
    "capo_securityhub.types.batch_update_findings_unprocessed_finding.BatchUpdateFindingsUnprocessedFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsUnprocessedFindingsList) -> list:
    import capo_securityhub.types.batch_update_findings_unprocessed_finding

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.batch_update_findings_unprocessed_finding.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateFindingsUnprocessedFindingsList:
    import capo_securityhub.types.batch_update_findings_unprocessed_finding

    out: BatchUpdateFindingsUnprocessedFindingsList = []
    for item in data:
        out.append(
            capo_securityhub.types.batch_update_findings_unprocessed_finding.deserialize_json(
                item
            )
        )
    return out
