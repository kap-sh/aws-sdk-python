"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_security_finding_identifier_list
    import capo_securityhub.types.batch_update_findings_unprocessed_findings_list


class BatchUpdateFindingsResponse(TypedDict, closed=True):
    processed_findings: NotRequired[
        "capo_securityhub.types.aws_security_finding_identifier_list.AwsSecurityFindingIdentifierList"
    ]
    """<p>The list of findings that were updated successfully.</p>"""
    unprocessed_findings: NotRequired[
        "capo_securityhub.types.batch_update_findings_unprocessed_findings_list.BatchUpdateFindingsUnprocessedFindingsList"
    ]
    """<p>The list of findings that were not updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsResponse) -> dict:
    out: dict = {}
    if "processed_findings" in value:
        import capo_securityhub.types.aws_security_finding_identifier_list

        out["ProcessedFindings"] = (
            capo_securityhub.types.aws_security_finding_identifier_list.serialize_json(
                value["processed_findings"]
            )
        )
    if "unprocessed_findings" in value:
        import capo_securityhub.types.batch_update_findings_unprocessed_findings_list

        out["UnprocessedFindings"] = (
            capo_securityhub.types.batch_update_findings_unprocessed_findings_list.serialize_json(
                value["unprocessed_findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateFindingsResponse:
    out: BatchUpdateFindingsResponse = {}  # type: ignore[typeddict-item]
    if "ProcessedFindings" in data:
        import capo_securityhub.types.aws_security_finding_identifier_list

        out["processed_findings"] = (
            capo_securityhub.types.aws_security_finding_identifier_list.deserialize_json(
                data["ProcessedFindings"]
            )
        )
    if "UnprocessedFindings" in data:
        import capo_securityhub.types.batch_update_findings_unprocessed_findings_list

        out["unprocessed_findings"] = (
            capo_securityhub.types.batch_update_findings_unprocessed_findings_list.deserialize_json(
                data["UnprocessedFindings"]
            )
        )
    return out
