"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListTrailsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.string
    import aws_sdk_cloudtrail.types.trails


class ListTrailsResponse(TypedDict):
    trails: NotRequired["aws_sdk_cloudtrail.types.trails.Trails"]
    """<p>Returns the name, ARN, and home Region of trails in the current account.</p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The token to use to get the next page of results after a previous API call. If the token does not appear, there are no more results to return. The token must be passed in with the same parameters as the previous call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrailsResponse) -> dict:
    out: dict = {}
    if "trails" in value:
        import aws_sdk_cloudtrail.types.trails

        out["Trails"] = aws_sdk_cloudtrail.types.trails.serialize_aws_json_1_1(
            value["trails"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrailsResponse:
    out: ListTrailsResponse = {}  # type: ignore[typeddict-item]
    if "Trails" in data:
        import aws_sdk_cloudtrail.types.trails

        out["trails"] = aws_sdk_cloudtrail.types.trails.deserialize_aws_json_1_1(
            data["Trails"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
