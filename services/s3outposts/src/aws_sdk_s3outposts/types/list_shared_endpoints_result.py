"""Generated from Smithy shape ``com.amazonaws.s3outposts#ListSharedEndpointsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3outposts.types.endpoints
    import aws_sdk_s3outposts.types.next_token


class ListSharedEndpointsResult(TypedDict, closed=True):
    endpoints: NotRequired["aws_sdk_s3outposts.types.endpoints.Endpoints"]
    """<p>The list of endpoints associated with the specified Outpost that have been shared by Amazon Web Services Resource Access Manager (RAM).</p>"""
    next_token: NotRequired["aws_sdk_s3outposts.types.next_token.NextToken"]
    """<p>If the number of endpoints associated with the specified Outpost exceeds <code>MaxResults</code>, you can include this value in subsequent calls to this operation to retrieve more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSharedEndpointsResult) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import aws_sdk_s3outposts.types.endpoints

        out["Endpoints"] = aws_sdk_s3outposts.types.endpoints.serialize_json(
            value["endpoints"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSharedEndpointsResult:
    out: ListSharedEndpointsResult = {}  # type: ignore[typeddict-item]
    if "Endpoints" in data:
        import aws_sdk_s3outposts.types.endpoints

        out["endpoints"] = aws_sdk_s3outposts.types.endpoints.deserialize_json(
            data["Endpoints"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
