"""Generated from Smithy shape ``com.amazonaws.kendra#AttributeSuggestionsGetConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.attribute_filter
    import aws_sdk_kendra.types.document_attribute_key_list
    import aws_sdk_kendra.types.user_context


class AttributeSuggestionsGetConfig(TypedDict):
    suggestion_attributes: NotRequired[
        "aws_sdk_kendra.types.document_attribute_key_list.DocumentAttributeKeyList"
    ]
    """<p>The list of document field/attribute keys or field names to use for query suggestions. If the content within any of the fields match what your user starts typing as their query, then the field content is returned as a query suggestion.</p>"""
    additional_response_attributes: NotRequired[
        "aws_sdk_kendra.types.document_attribute_key_list.DocumentAttributeKeyList"
    ]
    """<p>The list of additional document field/attribute keys or field names to include in the response. You can use additional fields to provide extra information in the response. Additional fields are not used to based suggestions on.</p>"""
    attribute_filter: NotRequired[
        "aws_sdk_kendra.types.attribute_filter.AttributeFilter"
    ]
    """<p>Filters the search results based on document fields/attributes.</p>"""
    user_context: NotRequired["aws_sdk_kendra.types.user_context.UserContext"]
    """<p>Applies user context filtering so that only users who are given access to certain documents see these document in their search results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeSuggestionsGetConfig) -> dict:
    out: dict = {}
    if "suggestion_attributes" in value:
        import aws_sdk_kendra.types.document_attribute_key_list

        out["SuggestionAttributes"] = (
            aws_sdk_kendra.types.document_attribute_key_list.serialize_aws_json_1_1(
                value["suggestion_attributes"]
            )
        )
    if "additional_response_attributes" in value:
        import aws_sdk_kendra.types.document_attribute_key_list

        out["AdditionalResponseAttributes"] = (
            aws_sdk_kendra.types.document_attribute_key_list.serialize_aws_json_1_1(
                value["additional_response_attributes"]
            )
        )
    if "attribute_filter" in value:
        import aws_sdk_kendra.types.attribute_filter

        out["AttributeFilter"] = (
            aws_sdk_kendra.types.attribute_filter.serialize_aws_json_1_1(
                value["attribute_filter"]
            )
        )
    if "user_context" in value:
        import aws_sdk_kendra.types.user_context

        out["UserContext"] = aws_sdk_kendra.types.user_context.serialize_aws_json_1_1(
            value["user_context"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeSuggestionsGetConfig:
    out: AttributeSuggestionsGetConfig = {}  # type: ignore[typeddict-item]
    if "SuggestionAttributes" in data:
        import aws_sdk_kendra.types.document_attribute_key_list

        out["suggestion_attributes"] = (
            aws_sdk_kendra.types.document_attribute_key_list.deserialize_aws_json_1_1(
                data["SuggestionAttributes"]
            )
        )
    if "AdditionalResponseAttributes" in data:
        import aws_sdk_kendra.types.document_attribute_key_list

        out["additional_response_attributes"] = (
            aws_sdk_kendra.types.document_attribute_key_list.deserialize_aws_json_1_1(
                data["AdditionalResponseAttributes"]
            )
        )
    if "AttributeFilter" in data:
        import aws_sdk_kendra.types.attribute_filter

        out["attribute_filter"] = (
            aws_sdk_kendra.types.attribute_filter.deserialize_aws_json_1_1(
                data["AttributeFilter"]
            )
        )
    if "UserContext" in data:
        import aws_sdk_kendra.types.user_context

        out["user_context"] = (
            aws_sdk_kendra.types.user_context.deserialize_aws_json_1_1(
                data["UserContext"]
            )
        )
    return out
