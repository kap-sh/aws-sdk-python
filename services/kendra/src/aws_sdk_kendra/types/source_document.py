"""Generated from Smithy shape ``com.amazonaws.kendra#SourceDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_attribute_key_list
    import aws_sdk_kendra.types.document_attribute_list
    import aws_sdk_kendra.types.string


class SourceDocument(TypedDict, closed=True):
    document_id: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>The identifier of the document used for a query suggestion.</p>"""
    suggestion_attributes: NotRequired[
        "aws_sdk_kendra.types.document_attribute_key_list.DocumentAttributeKeyList"
    ]
    """<p>The document fields/attributes used for a query suggestion.</p>"""
    additional_attributes: NotRequired[
        "aws_sdk_kendra.types.document_attribute_list.DocumentAttributeList"
    ]
    """<p>The additional fields/attributes to include in the response. You can use additional fields to provide extra information in the response. Additional fields are not used to based suggestions on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceDocument) -> dict:
    out: dict = {}
    if "document_id" in value:
        out["DocumentId"] = value["document_id"]
    if "suggestion_attributes" in value:
        import aws_sdk_kendra.types.document_attribute_key_list

        out["SuggestionAttributes"] = (
            aws_sdk_kendra.types.document_attribute_key_list.serialize_aws_json_1_1(
                value["suggestion_attributes"]
            )
        )
    if "additional_attributes" in value:
        import aws_sdk_kendra.types.document_attribute_list

        out["AdditionalAttributes"] = (
            aws_sdk_kendra.types.document_attribute_list.serialize_aws_json_1_1(
                value["additional_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceDocument:
    out: SourceDocument = {}  # type: ignore[typeddict-item]
    if "DocumentId" in data:
        out["document_id"] = data["DocumentId"]
    if "SuggestionAttributes" in data:
        import aws_sdk_kendra.types.document_attribute_key_list

        out["suggestion_attributes"] = (
            aws_sdk_kendra.types.document_attribute_key_list.deserialize_aws_json_1_1(
                data["SuggestionAttributes"]
            )
        )
    if "AdditionalAttributes" in data:
        import aws_sdk_kendra.types.document_attribute_list

        out["additional_attributes"] = (
            aws_sdk_kendra.types.document_attribute_list.deserialize_aws_json_1_1(
                data["AdditionalAttributes"]
            )
        )
    return out
