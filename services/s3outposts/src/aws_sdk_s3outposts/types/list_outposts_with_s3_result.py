"""Generated from Smithy shape ``com.amazonaws.s3outposts#ListOutpostsWithS3Result``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3outposts.types.next_token
    import aws_sdk_s3outposts.types.outposts


class ListOutpostsWithS3Result(TypedDict):
    outposts: NotRequired["aws_sdk_s3outposts.types.outposts.Outposts"]
    """<p>Returns the list of Outposts that have the following characteristics:</p> <ul> <li> <p>outposts that have S3 provisioned</p> </li> <li> <p>outposts that are <code>Active</code> (not pending any provisioning nor decommissioned)</p> </li> <li> <p>outposts to which the the calling Amazon Web Services account has access</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_s3outposts.types.next_token.NextToken"]
    """<p>Returns a token that you can use to call <code>ListOutpostsWithS3</code> again and receive additional results, if there are any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOutpostsWithS3Result) -> dict:
    out: dict = {}
    if "outposts" in value:
        import aws_sdk_s3outposts.types.outposts

        out["Outposts"] = aws_sdk_s3outposts.types.outposts.serialize_json(
            value["outposts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOutpostsWithS3Result:
    out: ListOutpostsWithS3Result = {}  # type: ignore[typeddict-item]
    if "Outposts" in data:
        import aws_sdk_s3outposts.types.outposts

        out["outposts"] = aws_sdk_s3outposts.types.outposts.deserialize_json(
            data["Outposts"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
