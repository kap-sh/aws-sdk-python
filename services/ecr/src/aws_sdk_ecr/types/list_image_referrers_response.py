"""Generated from Smithy shape ``com.amazonaws.ecr#ListImageReferrersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_referrer_list
    import aws_sdk_ecr.types.next_token


class ListImageReferrersResponse(TypedDict, closed=True):
    referrers: NotRequired["aws_sdk_ecr.types.image_referrer_list.ImageReferrerList"]
    """<p>The list of artifacts associated with the subject image.</p>"""
    next_token: NotRequired["aws_sdk_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListImageReferrers</code> request. When the results of a <code>ListImageReferrers</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImageReferrersResponse) -> dict:
    out: dict = {}
    if "referrers" in value:
        import aws_sdk_ecr.types.image_referrer_list

        out["referrers"] = aws_sdk_ecr.types.image_referrer_list.serialize_aws_json_1_1(
            value["referrers"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImageReferrersResponse:
    out: ListImageReferrersResponse = {}  # type: ignore[typeddict-item]
    if "referrers" in data:
        import aws_sdk_ecr.types.image_referrer_list

        out["referrers"] = (
            aws_sdk_ecr.types.image_referrer_list.deserialize_aws_json_1_1(
                data["referrers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
