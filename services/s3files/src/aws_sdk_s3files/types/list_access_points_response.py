"""Generated from Smithy shape ``com.amazonaws.s3files#ListAccessPointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3files.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3files.types.access_points


class ListAccessPointsResponse(TypedDict):
    next_token: NotRequired["str"]
    """<p>A pagination token to use in a subsequent request if more results are available.</p>"""
    access_points: "aws_sdk_s3files.types.access_points.AccessPoints"
    """<p>An array of access point descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPointsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_s3files.types.access_points

    out["accessPoints"] = aws_sdk_s3files.types.access_points.serialize_json(
        value["access_points"]
    )
    return out


def deserialize_json(data: dict) -> ListAccessPointsResponse:
    out: ListAccessPointsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "accessPoints" in data:
        import aws_sdk_s3files.types.access_points

        out["access_points"] = aws_sdk_s3files.types.access_points.deserialize_json(
            data["accessPoints"]
        )
    else:
        raise DeserializationError("ListAccessPointsResponse.access_points required")
    return out
