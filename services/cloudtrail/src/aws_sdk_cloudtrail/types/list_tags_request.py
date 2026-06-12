"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.resource_id_list
    import aws_sdk_cloudtrail.types.string


class ListTagsRequest(TypedDict):
    resource_id_list: "aws_sdk_cloudtrail.types.resource_id_list.ResourceIdList"
    """<p>Specifies a list of trail, event data store, dashboard, or channel ARNs whose tags will be listed. The list has a limit of 20 ARNs.</p> <p> Example trail ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p> <p>Example event data store ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE</code> </p> <p>Example dashboard ARN format: <code>arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash</code> </p> <p>Example channel ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890</code> </p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsRequest) -> dict:
    out: dict = {}
    import aws_sdk_cloudtrail.types.resource_id_list

    out["ResourceIdList"] = (
        aws_sdk_cloudtrail.types.resource_id_list.serialize_aws_json_1_1(
            value["resource_id_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    if "ResourceIdList" in data:
        import aws_sdk_cloudtrail.types.resource_id_list

        out["resource_id_list"] = (
            aws_sdk_cloudtrail.types.resource_id_list.deserialize_aws_json_1_1(
                data["ResourceIdList"]
            )
        )
    else:
        raise DeserializationError("ListTagsRequest.resource_id_list required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
