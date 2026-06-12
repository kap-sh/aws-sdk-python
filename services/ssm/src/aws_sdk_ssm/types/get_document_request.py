"""Generated from Smithy shape ``com.amazonaws.ssm#GetDocumentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_arn
    import aws_sdk_ssm.types.document_format
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.document_version_name


class GetDocumentRequest(TypedDict):
    name: "aws_sdk_ssm.types.document_arn.DocumentARN"
    """<p>The name of the SSM document.</p>"""
    version_name: NotRequired[
        "aws_sdk_ssm.types.document_version_name.DocumentVersionName"
    ]
    """<p>An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document and can't be changed.</p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The document version for which you want information.</p>"""
    document_format: NotRequired["aws_sdk_ssm.types.document_format.DocumentFormat"]
    """<p>Returns the document in the specified format. The document format can be either JSON or YAML. JSON is the default format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDocumentRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "document_format" in value:
        import aws_sdk_ssm.types.document_format

        out["DocumentFormat"] = (
            aws_sdk_ssm.types.document_format.serialize_aws_json_1_1(
                value["document_format"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDocumentRequest:
    out: GetDocumentRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetDocumentRequest.name required")
    if "VersionName" in data:
        out["version_name"] = data["VersionName"]
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "DocumentFormat" in data:
        import aws_sdk_ssm.types.document_format

        out["document_format"] = (
            aws_sdk_ssm.types.document_format.deserialize_aws_json_1_1(
                data["DocumentFormat"]
            )
        )
    return out
