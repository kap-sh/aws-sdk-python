"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentDefaultVersionDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_name
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.document_version_name


class DocumentDefaultVersionDescription(TypedDict):
    name: NotRequired["aws_sdk_ssm.types.document_name.DocumentName"]
    """<p>The name of the document.</p>"""
    default_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The default version of the document.</p>"""
    default_version_name: NotRequired[
        "aws_sdk_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>The default version of the artifact associated with the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentDefaultVersionDescription) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "default_version" in value:
        out["DefaultVersion"] = value["default_version"]
    if "default_version_name" in value:
        out["DefaultVersionName"] = value["default_version_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentDefaultVersionDescription:
    out: DocumentDefaultVersionDescription = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DefaultVersion" in data:
        out["default_version"] = data["DefaultVersion"]
    if "DefaultVersionName" in data:
        out["default_version_name"] = data["DefaultVersionName"]
    return out
