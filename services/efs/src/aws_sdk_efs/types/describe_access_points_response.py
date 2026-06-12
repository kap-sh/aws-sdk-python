"""Generated from Smithy shape ``com.amazonaws.efs#DescribeAccessPointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.access_point_descriptions
    import aws_sdk_efs.types.token


class DescribeAccessPointsResponse(TypedDict):
    access_points: NotRequired[
        "aws_sdk_efs.types.access_point_descriptions.AccessPointDescriptions"
    ]
    """<p>An array of access point descriptions.</p>"""
    next_token: NotRequired["aws_sdk_efs.types.token.Token"]
    """<p>Present if there are more access points than returned in the response. You can use the NextMarker in the subsequent request to fetch the additional descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccessPointsResponse) -> dict:
    out: dict = {}
    if "access_points" in value:
        import aws_sdk_efs.types.access_point_descriptions

        out["AccessPoints"] = (
            aws_sdk_efs.types.access_point_descriptions.serialize_json(
                value["access_points"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeAccessPointsResponse:
    out: DescribeAccessPointsResponse = {}  # type: ignore[typeddict-item]
    if "AccessPoints" in data:
        import aws_sdk_efs.types.access_point_descriptions

        out["access_points"] = (
            aws_sdk_efs.types.access_point_descriptions.deserialize_json(
                data["AccessPoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
