"""Generated from Smithy shape ``com.amazonaws.interconnect#ListAttachPointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.attach_point_descriptor_list
    import aws_sdk_interconnect.types.next_token


class ListAttachPointsResponse(TypedDict, closed=True):
    attach_points: "aws_sdk_interconnect.types.attach_point_descriptor_list.AttachPointDescriptorList"
    """<p>The valid <a>AttachPoint</a> </p>"""
    next_token: NotRequired["aws_sdk_interconnect.types.next_token.NextToken"]
    """<p>A pagination token indicating that there are more results that can be fetched.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAttachPointsResponse) -> dict:
    out: dict = {}
    import aws_sdk_interconnect.types.attach_point_descriptor_list

    out["attachPoints"] = (
        aws_sdk_interconnect.types.attach_point_descriptor_list.serialize_aws_json_1_0(
            value["attach_points"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAttachPointsResponse:
    out: ListAttachPointsResponse = {}  # type: ignore[typeddict-item]
    if "attachPoints" in data:
        import aws_sdk_interconnect.types.attach_point_descriptor_list

        out["attach_points"] = (
            aws_sdk_interconnect.types.attach_point_descriptor_list.deserialize_aws_json_1_0(
                data["attachPoints"]
            )
        )
    else:
        raise DeserializationError("ListAttachPointsResponse.attach_points required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
