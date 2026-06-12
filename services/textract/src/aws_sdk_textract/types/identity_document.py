"""Generated from Smithy shape ``com.amazonaws.textract#IdentityDocument``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.block_list
    import aws_sdk_textract.types.identity_document_field_list
    import aws_sdk_textract.types.u_integer


class IdentityDocument(TypedDict):
    document_index: NotRequired["aws_sdk_textract.types.u_integer.UInteger"]
    """<p>Denotes the placement of a document in the IdentityDocument list. The first document is marked 1, the second 2 and so on.</p>"""
    identity_document_fields: NotRequired[
        "aws_sdk_textract.types.identity_document_field_list.IdentityDocumentFieldList"
    ]
    """<p>The structure used to record information extracted from identity documents. Contains both normalized field and value of the extracted text.</p>"""
    blocks: NotRequired["aws_sdk_textract.types.block_list.BlockList"]
    """<p>Individual word recognition, as returned by document detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityDocument) -> dict:
    out: dict = {}
    if "document_index" in value:
        out["DocumentIndex"] = value["document_index"]
    if "identity_document_fields" in value:
        import aws_sdk_textract.types.identity_document_field_list

        out["IdentityDocumentFields"] = (
            aws_sdk_textract.types.identity_document_field_list.serialize_aws_json_1_1(
                value["identity_document_fields"]
            )
        )
    if "blocks" in value:
        import aws_sdk_textract.types.block_list

        out["Blocks"] = aws_sdk_textract.types.block_list.serialize_aws_json_1_1(
            value["blocks"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityDocument:
    out: IdentityDocument = {}  # type: ignore[typeddict-item]
    if "DocumentIndex" in data:
        out["document_index"] = data["DocumentIndex"]
    if "IdentityDocumentFields" in data:
        import aws_sdk_textract.types.identity_document_field_list

        out["identity_document_fields"] = (
            aws_sdk_textract.types.identity_document_field_list.deserialize_aws_json_1_1(
                data["IdentityDocumentFields"]
            )
        )
    if "Blocks" in data:
        import aws_sdk_textract.types.block_list

        out["blocks"] = aws_sdk_textract.types.block_list.deserialize_aws_json_1_1(
            data["Blocks"]
        )
    return out
