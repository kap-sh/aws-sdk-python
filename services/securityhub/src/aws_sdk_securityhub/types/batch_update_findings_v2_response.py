"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.batch_update_findings_v2_processed_findings_list
    import aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_findings_list


class BatchUpdateFindingsV2Response(TypedDict, closed=True):
    processed_findings: NotRequired[
        "aws_sdk_securityhub.types.batch_update_findings_v2_processed_findings_list.BatchUpdateFindingsV2ProcessedFindingsList"
    ]
    """<p>The list of findings that were updated successfully.</p>"""
    unprocessed_findings: NotRequired[
        "aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_findings_list.BatchUpdateFindingsV2UnprocessedFindingsList"
    ]
    """<p>The list of V2 findings that were not updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsV2Response) -> dict:
    out: dict = {}
    if "processed_findings" in value:
        import aws_sdk_securityhub.types.batch_update_findings_v2_processed_findings_list

        out["ProcessedFindings"] = (
            aws_sdk_securityhub.types.batch_update_findings_v2_processed_findings_list.serialize_json(
                value["processed_findings"]
            )
        )
    if "unprocessed_findings" in value:
        import aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_findings_list

        out["UnprocessedFindings"] = (
            aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_findings_list.serialize_json(
                value["unprocessed_findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateFindingsV2Response:
    out: BatchUpdateFindingsV2Response = {}  # type: ignore[typeddict-item]
    if "ProcessedFindings" in data:
        import aws_sdk_securityhub.types.batch_update_findings_v2_processed_findings_list

        out["processed_findings"] = (
            aws_sdk_securityhub.types.batch_update_findings_v2_processed_findings_list.deserialize_json(
                data["ProcessedFindings"]
            )
        )
    if "UnprocessedFindings" in data:
        import aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_findings_list

        out["unprocessed_findings"] = (
            aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_findings_list.deserialize_json(
                data["UnprocessedFindings"]
            )
        )
    return out
