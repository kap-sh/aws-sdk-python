"""Generated from Smithy shape ``com.amazonaws.ssm#ListAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_filter_list
    import aws_sdk_ssm.types.max_results
    import aws_sdk_ssm.types.next_token


class ListAssociationsRequest(TypedDict, closed=True):
    association_filter_list: NotRequired[
        "aws_sdk_ssm.types.association_filter_list.AssociationFilterList"
    ]
    """<p>One or more filters. Use a filter to return a more specific list of results.</p> <note> <p>Filtering associations using the <code>InstanceID</code> attribute only returns legacy associations created using the <code>InstanceID</code> attribute. Associations targeting the managed node that are part of the Target Attributes <code>ResourceGroup</code> or <code>Tags</code> aren't returned.</p> </note>"""
    max_results: NotRequired["aws_sdk_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssociationsRequest) -> dict:
    out: dict = {}
    if "association_filter_list" in value:
        import aws_sdk_ssm.types.association_filter_list

        out["AssociationFilterList"] = (
            aws_sdk_ssm.types.association_filter_list.serialize_aws_json_1_1(
                value["association_filter_list"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssociationsRequest:
    out: ListAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "AssociationFilterList" in data:
        import aws_sdk_ssm.types.association_filter_list

        out["association_filter_list"] = (
            aws_sdk_ssm.types.association_filter_list.deserialize_aws_json_1_1(
                data["AssociationFilterList"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
