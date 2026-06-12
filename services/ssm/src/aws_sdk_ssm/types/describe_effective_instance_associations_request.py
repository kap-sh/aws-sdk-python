"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeEffectiveInstanceAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.effective_instance_association_max_results
    import aws_sdk_ssm.types.instance_id
    import aws_sdk_ssm.types.next_token


class DescribeEffectiveInstanceAssociationsRequest(TypedDict):
    instance_id: "aws_sdk_ssm.types.instance_id.InstanceId"
    """<p>The managed node ID for which you want to view all associations.</p>"""
    max_results: NotRequired[
        "aws_sdk_ssm.types.effective_instance_association_max_results.EffectiveInstanceAssociationMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEffectiveInstanceAssociationsRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeEffectiveInstanceAssociationsRequest:
    out: DescribeEffectiveInstanceAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "DescribeEffectiveInstanceAssociationsRequest.instance_id required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
