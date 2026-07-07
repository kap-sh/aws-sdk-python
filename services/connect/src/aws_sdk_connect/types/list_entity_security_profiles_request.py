"""Generated from Smithy shape ``com.amazonaws.connect#ListEntitySecurityProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.entity_arn
    import aws_sdk_connect.types.entity_type
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result100
    import aws_sdk_connect.types.next_token2500


class ListEntitySecurityProfilesRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p> The identifier of the Amazon Connect instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance. </p>"""
    entity_type: "aws_sdk_connect.types.entity_type.EntityType"
    """<p> Only supported type is AI_AGENT. </p>"""
    entity_arn: "aws_sdk_connect.types.entity_arn.EntityArn"
    """<p> ARN of a Q in Connect AI Agent. </p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token2500.NextToken2500"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result100.MaxResult100"]
    """<p> The maximum number of results to return per page. The default MaxResult size is 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitySecurityProfilesRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.entity_type

    out["EntityType"] = aws_sdk_connect.types.entity_type.serialize_json(
        value["entity_type"]
    )
    out["EntityArn"] = value["entity_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListEntitySecurityProfilesRequest:
    out: ListEntitySecurityProfilesRequest = {}  # type: ignore[typeddict-item]
    if "EntityType" in data:
        import aws_sdk_connect.types.entity_type

        out["entity_type"] = aws_sdk_connect.types.entity_type.deserialize_json(
            data["EntityType"]
        )
    else:
        raise DeserializationError(
            "ListEntitySecurityProfilesRequest.entity_type required"
        )
    if "EntityArn" in data:
        out["entity_arn"] = data["EntityArn"]
    else:
        raise DeserializationError(
            "ListEntitySecurityProfilesRequest.entity_arn required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
