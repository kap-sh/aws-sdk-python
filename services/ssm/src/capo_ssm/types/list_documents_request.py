"""Generated from Smithy shape ``com.amazonaws.ssm#ListDocumentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_filter_list
    import capo_ssm.types.document_key_values_filter_list
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token


class ListDocumentsRequest(TypedDict, closed=True):
    document_filter_list: NotRequired[
        "capo_ssm.types.document_filter_list.DocumentFilterList"
    ]
    """<p>This data type is deprecated. Instead, use <code>Filters</code>.</p>"""
    filters: NotRequired[
        "capo_ssm.types.document_key_values_filter_list.DocumentKeyValuesFilterList"
    ]
    """<p>One or more <code>DocumentKeyValuesFilter</code> objects. Use a filter to return a more specific list of results. For keys, you can specify one or more key-value pair tags that have been applied to a document. Other valid keys include <code>Owner</code>, <code>Name</code>, <code>PlatformTypes</code>, <code>DocumentType</code>, and <code>TargetType</code>. For example, to return documents you own use <code>Key=Owner,Values=Self</code>. To specify a custom key-value pair, use the format <code>Key=tag:tagName,Values=valueName</code>.</p> <note> <p>This API operation only supports filtering documents by using a single tag key and one or more tag values. For example: <code>Key=tag:tagName,Values=valueName1,valueName2</code> </p> </note>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentsRequest) -> dict:
    out: dict = {}
    if "document_filter_list" in value:
        import capo_ssm.types.document_filter_list

        out["DocumentFilterList"] = (
            capo_ssm.types.document_filter_list.serialize_aws_json_1_1(
                value["document_filter_list"]
            )
        )
    if "filters" in value:
        import capo_ssm.types.document_key_values_filter_list

        out["Filters"] = (
            capo_ssm.types.document_key_values_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentsRequest:
    out: ListDocumentsRequest = {}  # type: ignore[typeddict-item]
    if "DocumentFilterList" in data:
        import capo_ssm.types.document_filter_list

        out["document_filter_list"] = (
            capo_ssm.types.document_filter_list.deserialize_aws_json_1_1(
                data["DocumentFilterList"]
            )
        )
    if "Filters" in data:
        import capo_ssm.types.document_key_values_filter_list

        out["filters"] = (
            capo_ssm.types.document_key_values_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
