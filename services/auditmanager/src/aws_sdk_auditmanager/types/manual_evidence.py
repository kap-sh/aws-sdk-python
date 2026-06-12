"""Generated from Smithy shape ``com.amazonaws.auditmanager#ManualEvidence``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.manual_evidence_local_file_name
    import aws_sdk_auditmanager.types.manual_evidence_text_response
    import aws_sdk_auditmanager.types.s3_url


class ManualEvidence(TypedDict):
    s3_resource_path: NotRequired["aws_sdk_auditmanager.types.s3_url.S3Url"]
    """<p>The S3 URL of the object that's imported as manual evidence. </p>"""
    text_response: NotRequired[
        "aws_sdk_auditmanager.types.manual_evidence_text_response.ManualEvidenceTextResponse"
    ]
    """<p>The plain text response that's entered and saved as manual evidence.</p>"""
    evidence_file_name: NotRequired[
        "aws_sdk_auditmanager.types.manual_evidence_local_file_name.ManualEvidenceLocalFileName"
    ]
    """<p>The name of the file that's uploaded as manual evidence. This name is populated using the <code>evidenceFileName</code> value from the <a href=\"https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFileUploadUrl.html\"> <code>GetEvidenceFileUploadUrl</code> </a> API response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManualEvidence) -> dict:
    out: dict = {}
    if "s3_resource_path" in value:
        out["s3ResourcePath"] = value["s3_resource_path"]
    if "text_response" in value:
        out["textResponse"] = value["text_response"]
    if "evidence_file_name" in value:
        out["evidenceFileName"] = value["evidence_file_name"]
    return out


def deserialize_json(data: dict) -> ManualEvidence:
    out: ManualEvidence = {}  # type: ignore[typeddict-item]
    if "s3ResourcePath" in data:
        out["s3_resource_path"] = data["s3ResourcePath"]
    if "textResponse" in data:
        out["text_response"] = data["textResponse"]
    if "evidenceFileName" in data:
        out["evidence_file_name"] = data["evidenceFileName"]
    return out
