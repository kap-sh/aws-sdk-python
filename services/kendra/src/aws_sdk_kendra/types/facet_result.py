"""Generated from Smithy shape ``com.amazonaws.kendra#FacetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_attribute_key
    import aws_sdk_kendra.types.document_attribute_value_count_pair_list
    import aws_sdk_kendra.types.document_attribute_value_type


class FacetResult(TypedDict, closed=True):
    document_attribute_key: NotRequired[
        "aws_sdk_kendra.types.document_attribute_key.DocumentAttributeKey"
    ]
    """<p>The key for the facet values. This is the same as the <code>DocumentAttributeKey</code> provided in the query.</p>"""
    document_attribute_value_type: NotRequired[
        "aws_sdk_kendra.types.document_attribute_value_type.DocumentAttributeValueType"
    ]
    """<p>The data type of the facet value. This is the same as the type defined for the index field when it was created.</p>"""
    document_attribute_value_count_pairs: NotRequired[
        "aws_sdk_kendra.types.document_attribute_value_count_pair_list.DocumentAttributeValueCountPairList"
    ]
    """<p>An array of key/value pairs, where the key is the value of the attribute and the count is the number of documents that share the key value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FacetResult) -> dict:
    out: dict = {}
    if "document_attribute_key" in value:
        out["DocumentAttributeKey"] = value["document_attribute_key"]
    if "document_attribute_value_type" in value:
        import aws_sdk_kendra.types.document_attribute_value_type

        out["DocumentAttributeValueType"] = (
            aws_sdk_kendra.types.document_attribute_value_type.serialize_aws_json_1_1(
                value["document_attribute_value_type"]
            )
        )
    if "document_attribute_value_count_pairs" in value:
        import aws_sdk_kendra.types.document_attribute_value_count_pair_list

        out["DocumentAttributeValueCountPairs"] = (
            aws_sdk_kendra.types.document_attribute_value_count_pair_list.serialize_aws_json_1_1(
                value["document_attribute_value_count_pairs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FacetResult:
    out: FacetResult = {}  # type: ignore[typeddict-item]
    if "DocumentAttributeKey" in data:
        out["document_attribute_key"] = data["DocumentAttributeKey"]
    if "DocumentAttributeValueType" in data:
        import aws_sdk_kendra.types.document_attribute_value_type

        out["document_attribute_value_type"] = (
            aws_sdk_kendra.types.document_attribute_value_type.deserialize_aws_json_1_1(
                data["DocumentAttributeValueType"]
            )
        )
    if "DocumentAttributeValueCountPairs" in data:
        import aws_sdk_kendra.types.document_attribute_value_count_pair_list

        out["document_attribute_value_count_pairs"] = (
            aws_sdk_kendra.types.document_attribute_value_count_pair_list.deserialize_aws_json_1_1(
                data["DocumentAttributeValueCountPairs"]
            )
        )
    return out
