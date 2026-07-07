"""Generated from Smithy shape ``com.amazonaws.wisdom#StartImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.content_metadata
    import aws_sdk_wisdom.types.external_source_configuration
    import aws_sdk_wisdom.types.import_job_type
    import aws_sdk_wisdom.types.non_empty_string
    import aws_sdk_wisdom.types.upload_id
    import aws_sdk_wisdom.types.uuid_or_arn


class StartImportJobRequest(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p> <ul> <li> <p>For importing Wisdom quick responses, this should be a <code>QUICK_RESPONSES</code> type knowledge base.</p> </li> </ul>"""
    import_job_type: "aws_sdk_wisdom.types.import_job_type.ImportJobType"
    """<p>The type of the import job.</p> <ul> <li> <p>For importing quick response resource, set the value to <code>QUICK_RESPONSES</code>.</p> </li> </ul>"""
    upload_id: "aws_sdk_wisdom.types.upload_id.UploadId"
    r"""<p>A pointer to the uploaded asset. This value is returned by <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html\">StartContentUpload</a>.</p>"""
    client_token: NotRequired["aws_sdk_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    metadata: NotRequired["aws_sdk_wisdom.types.content_metadata.ContentMetadata"]
    """<p>The metadata fields of the imported Wisdom resources.</p>"""
    external_source_configuration: NotRequired[
        "aws_sdk_wisdom.types.external_source_configuration.ExternalSourceConfiguration"
    ]
    """<p>The configuration information of the external source that the resource data are imported from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportJobRequest) -> dict:
    out: dict = {}
    out["importJobType"] = value["import_job_type"]
    out["uploadId"] = value["upload_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "metadata" in value:
        import aws_sdk_wisdom.types.content_metadata

        out["metadata"] = aws_sdk_wisdom.types.content_metadata.serialize_json(
            value["metadata"]
        )
    if "external_source_configuration" in value:
        import aws_sdk_wisdom.types.external_source_configuration

        out["externalSourceConfiguration"] = (
            aws_sdk_wisdom.types.external_source_configuration.serialize_json(
                value["external_source_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartImportJobRequest:
    out: StartImportJobRequest = {}  # type: ignore[typeddict-item]
    if "importJobType" in data:
        out["import_job_type"] = data["importJobType"]
    else:
        raise DeserializationError("StartImportJobRequest.import_job_type required")
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("StartImportJobRequest.upload_id required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "metadata" in data:
        import aws_sdk_wisdom.types.content_metadata

        out["metadata"] = aws_sdk_wisdom.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    if "externalSourceConfiguration" in data:
        import aws_sdk_wisdom.types.external_source_configuration

        out["external_source_configuration"] = (
            aws_sdk_wisdom.types.external_source_configuration.deserialize_json(
                data["externalSourceConfiguration"]
            )
        )
    return out
