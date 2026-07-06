"""Generated from Smithy shape ``com.amazonaws.wisdom#SearchQuickResponsesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.contact_attributes
    import aws_sdk_wisdom.types.max_results
    import aws_sdk_wisdom.types.non_empty_string
    import aws_sdk_wisdom.types.quick_response_search_expression
    import aws_sdk_wisdom.types.uuid_or_arn


class SearchQuickResponsesRequest(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    search_expression: "aws_sdk_wisdom.types.quick_response_search_expression.QuickResponseSearchExpression"
    """<p>The search expression for querying the quick response.</p>"""
    next_token: NotRequired["aws_sdk_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_wisdom.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    attributes: NotRequired["aws_sdk_wisdom.types.contact_attributes.ContactAttributes"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/connect-attrib-list.html#user-defined-attributes\">user-defined Amazon Connect contact attributes</a> to be resolved when search results are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchQuickResponsesRequest) -> dict:
    out: dict = {}
    import aws_sdk_wisdom.types.quick_response_search_expression

    out["searchExpression"] = (
        aws_sdk_wisdom.types.quick_response_search_expression.serialize_json(
            value["search_expression"]
        )
    )
    if "attributes" in value:
        import aws_sdk_wisdom.types.contact_attributes

        out["attributes"] = aws_sdk_wisdom.types.contact_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> SearchQuickResponsesRequest:
    out: SearchQuickResponsesRequest = {}  # type: ignore[typeddict-item]
    if "searchExpression" in data:
        import aws_sdk_wisdom.types.quick_response_search_expression

        out["search_expression"] = (
            aws_sdk_wisdom.types.quick_response_search_expression.deserialize_json(
                data["searchExpression"]
            )
        )
    else:
        raise DeserializationError(
            "SearchQuickResponsesRequest.search_expression required"
        )
    if "attributes" in data:
        import aws_sdk_wisdom.types.contact_attributes

        out["attributes"] = aws_sdk_wisdom.types.contact_attributes.deserialize_json(
            data["attributes"]
        )
    return out
