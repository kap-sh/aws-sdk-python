"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateDocumentResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_description


class UpdateDocumentResult(TypedDict):
    document_description: NotRequired[
        "aws_sdk_ssm.types.document_description.DocumentDescription"
    ]
    """<p>A description of the document that was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDocumentResult) -> dict:
    out: dict = {}
    if "document_description" in value:
        import aws_sdk_ssm.types.document_description

        out["DocumentDescription"] = (
            aws_sdk_ssm.types.document_description.serialize_aws_json_1_1(
                value["document_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDocumentResult:
    out: UpdateDocumentResult = {}  # type: ignore[typeddict-item]
    if "DocumentDescription" in data:
        import aws_sdk_ssm.types.document_description

        out["document_description"] = (
            aws_sdk_ssm.types.document_description.deserialize_aws_json_1_1(
                data["DocumentDescription"]
            )
        )
    return out
