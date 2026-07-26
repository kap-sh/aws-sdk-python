"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAssociationExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.association_execution_filter_list
    import capo_ssm.types.association_id
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token


class DescribeAssociationExecutionsRequest(TypedDict, closed=True):
    association_id: "capo_ssm.types.association_id.AssociationId"
    """<p>The association ID for which you want to view execution history details.</p>"""
    filters: NotRequired[
        "capo_ssm.types.association_execution_filter_list.AssociationExecutionFilterList"
    ]
    """<p>Filters for the request. You can specify the following filters and values.</p> <p>ExecutionId (EQUAL)</p> <p>Status (EQUAL)</p> <p>CreatedTime (EQUAL, GREATER_THAN, LESS_THAN)</p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssociationExecutionsRequest) -> dict:
    out: dict = {}
    out["AssociationId"] = value["association_id"]
    if "filters" in value:
        import capo_ssm.types.association_execution_filter_list

        out["Filters"] = (
            capo_ssm.types.association_execution_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssociationExecutionsRequest:
    out: DescribeAssociationExecutionsRequest = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    else:
        raise DeserializationError(
            "DescribeAssociationExecutionsRequest.association_id required"
        )
    if "Filters" in data:
        import capo_ssm.types.association_execution_filter_list

        out["filters"] = (
            capo_ssm.types.association_execution_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
