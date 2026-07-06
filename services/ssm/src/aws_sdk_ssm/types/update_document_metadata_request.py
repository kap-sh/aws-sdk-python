"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateDocumentMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_name
    import aws_sdk_ssm.types.document_reviews
    import aws_sdk_ssm.types.document_version


class UpdateDocumentMetadataRequest(TypedDict, closed=True):
    name: "aws_sdk_ssm.types.document_name.DocumentName"
    """<p>The name of the change template for which a version's metadata is to be updated.</p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The version of a change template in which to update approval metadata.</p>"""
    document_reviews: "aws_sdk_ssm.types.document_reviews.DocumentReviews"
    """<p>The change template review details to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDocumentMetadataRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    import aws_sdk_ssm.types.document_reviews

    out["DocumentReviews"] = aws_sdk_ssm.types.document_reviews.serialize_aws_json_1_1(
        value["document_reviews"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDocumentMetadataRequest:
    out: UpdateDocumentMetadataRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDocumentMetadataRequest.name required")
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "DocumentReviews" in data:
        import aws_sdk_ssm.types.document_reviews

        out["document_reviews"] = (
            aws_sdk_ssm.types.document_reviews.deserialize_aws_json_1_1(
                data["DocumentReviews"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDocumentMetadataRequest.document_reviews required"
        )
    return out
