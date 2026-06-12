"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_security_finding_identifier_list
    import aws_sdk_securityhub.types.batch_update_findings_unprocessed_findings_list


class BatchUpdateFindingsResponse(TypedDict):
    processed_findings: NotRequired[
        "aws_sdk_securityhub.types.aws_security_finding_identifier_list.AwsSecurityFindingIdentifierList"
    ]
    """<p>The list of findings that were updated successfully.</p>"""
    unprocessed_findings: NotRequired[
        "aws_sdk_securityhub.types.batch_update_findings_unprocessed_findings_list.BatchUpdateFindingsUnprocessedFindingsList"
    ]
    """<p>The list of findings that were not updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsResponse) -> dict:
    out: dict = {}
    if "processed_findings" in value:
        import aws_sdk_securityhub.types.aws_security_finding_identifier_list

        out["ProcessedFindings"] = (
            aws_sdk_securityhub.types.aws_security_finding_identifier_list.serialize_json(
                value["processed_findings"]
            )
        )
    if "unprocessed_findings" in value:
        import aws_sdk_securityhub.types.batch_update_findings_unprocessed_findings_list

        out["UnprocessedFindings"] = (
            aws_sdk_securityhub.types.batch_update_findings_unprocessed_findings_list.serialize_json(
                value["unprocessed_findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateFindingsResponse:
    out: BatchUpdateFindingsResponse = {}  # type: ignore[typeddict-item]
    if "ProcessedFindings" in data:
        import aws_sdk_securityhub.types.aws_security_finding_identifier_list

        out["processed_findings"] = (
            aws_sdk_securityhub.types.aws_security_finding_identifier_list.deserialize_json(
                data["ProcessedFindings"]
            )
        )
    if "UnprocessedFindings" in data:
        import aws_sdk_securityhub.types.batch_update_findings_unprocessed_findings_list

        out["unprocessed_findings"] = (
            aws_sdk_securityhub.types.batch_update_findings_unprocessed_findings_list.deserialize_json(
                data["UnprocessedFindings"]
            )
        )
    return out
