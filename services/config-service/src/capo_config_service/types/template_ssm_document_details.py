"""Generated from Smithy shape ``com.amazonaws.configservice#TemplateSSMDocumentDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.ssm_document_name
    import capo_config_service.types.ssm_document_version


class TemplateSSMDocumentDetails(TypedDict, closed=True):
    document_name: "capo_config_service.types.ssm_document_name.SSMDocumentName"
    """<p>The name or Amazon Resource Name (ARN) of the SSM document to use to create a conformance pack. If you use the document name, Config checks only your account and Amazon Web Services Region for the SSM document.</p>"""
    document_version: NotRequired[
        "capo_config_service.types.ssm_document_version.SSMDocumentVersion"
    ]
    """<p>The version of the SSM document to use to create a conformance pack. By default, Config uses the latest version.</p> <note> <p>This field is optional.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TemplateSSMDocumentDetails) -> dict:
    out: dict = {}
    out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TemplateSSMDocumentDetails:
    out: TemplateSSMDocumentDetails = {}  # type: ignore[typeddict-item]
    if "DocumentName" in data:
        out["document_name"] = data["DocumentName"]
    else:
        raise DeserializationError("TemplateSSMDocumentDetails.document_name required")
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    return out
