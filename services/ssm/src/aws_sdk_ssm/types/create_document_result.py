"""Generated from Smithy shape ``com.amazonaws.ssm#CreateDocumentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_description


class CreateDocumentResult(TypedDict, closed=True):
    document_description: NotRequired[
        "aws_sdk_ssm.types.document_description.DocumentDescription"
    ]
    """<p>Information about the SSM document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDocumentResult) -> dict:
    out: dict = {}
    if "document_description" in value:
        import aws_sdk_ssm.types.document_description

        out["DocumentDescription"] = (
            aws_sdk_ssm.types.document_description.serialize_aws_json_1_1(
                value["document_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDocumentResult:
    out: CreateDocumentResult = {}  # type: ignore[typeddict-item]
    if "DocumentDescription" in data:
        import aws_sdk_ssm.types.document_description

        out["document_description"] = (
            aws_sdk_ssm.types.document_description.deserialize_aws_json_1_1(
                data["DocumentDescription"]
            )
        )
    return out
