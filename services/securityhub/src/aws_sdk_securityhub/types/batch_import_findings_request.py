"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchImportFindingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.batch_import_findings_request_finding_list


class BatchImportFindingsRequest(TypedDict):
    findings: NotRequired[
        "aws_sdk_securityhub.types.batch_import_findings_request_finding_list.BatchImportFindingsRequestFindingList"
    ]
    r"""<p>A list of findings to import. To successfully import a finding, it must follow the <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html\">Amazon Web Services Security Finding Format</a>. Maximum of 100 findings per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportFindingsRequest) -> dict:
    out: dict = {}
    if "findings" in value:
        import aws_sdk_securityhub.types.batch_import_findings_request_finding_list

        out["Findings"] = (
            aws_sdk_securityhub.types.batch_import_findings_request_finding_list.serialize_json(
                value["findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchImportFindingsRequest:
    out: BatchImportFindingsRequest = {}  # type: ignore[typeddict-item]
    if "Findings" in data:
        import aws_sdk_securityhub.types.batch_import_findings_request_finding_list

        out["findings"] = (
            aws_sdk_securityhub.types.batch_import_findings_request_finding_list.deserialize_json(
                data["Findings"]
            )
        )
    return out
