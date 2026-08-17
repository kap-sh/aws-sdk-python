"""Generated from Smithy shape ``com.amazonaws.ssm#CreateDocumentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_description


class CreateDocumentResult(TypedDict, closed=True):
    document_description: NotRequired[
        "capo_ssm.types.document_description.DocumentDescription"
    ]
    """<p>Information about the SSM document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDocumentResult) -> dict:
    out: dict = {}
    if "document_description" in value:
        import capo_ssm.types.document_description

        out["DocumentDescription"] = (
            capo_ssm.types.document_description.serialize_aws_json_1_1(
                value["document_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDocumentResult:
    out: CreateDocumentResult = {}  # type: ignore[typeddict-item]
    if data.get("DocumentDescription") is not None:
        import capo_ssm.types.document_description

        out["document_description"] = (
            capo_ssm.types.document_description.deserialize_aws_json_1_1(
                data["DocumentDescription"]
            )
        )
    return out
