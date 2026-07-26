"""Generated from Smithy shape ``com.amazonaws.efs#DescribeAccessPointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.access_point_descriptions
    import capo_efs.types.token


class DescribeAccessPointsResponse(TypedDict, closed=True):
    access_points: NotRequired[
        "capo_efs.types.access_point_descriptions.AccessPointDescriptions"
    ]
    """<p>An array of access point descriptions.</p>"""
    next_token: NotRequired["capo_efs.types.token.Token"]
    """<p>Present if there are more access points than returned in the response. You can use the NextMarker in the subsequent request to fetch the additional descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccessPointsResponse) -> dict:
    out: dict = {}
    if "access_points" in value:
        import capo_efs.types.access_point_descriptions

        out["AccessPoints"] = capo_efs.types.access_point_descriptions.serialize_json(
            value["access_points"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeAccessPointsResponse:
    out: DescribeAccessPointsResponse = {}  # type: ignore[typeddict-item]
    if "AccessPoints" in data:
        import capo_efs.types.access_point_descriptions

        out["access_points"] = (
            capo_efs.types.access_point_descriptions.deserialize_json(
                data["AccessPoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
