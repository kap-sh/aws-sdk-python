"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListPublicKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.string


class ListPublicKeysRequest(TypedDict, closed=True):
    start_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Optionally specifies, in UTC, the start of the time range to look up public keys for CloudTrail digest files. If not specified, the current time is used, and the current public key is returned.</p>"""
    end_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Optionally specifies, in UTC, the end of the time range to look up public keys for CloudTrail digest files. If not specified, the current time is used.</p>"""
    next_token: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPublicKeysRequest) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_cloudtrail.types.date

        out["StartTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_cloudtrail.types.date

        out["EndTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPublicKeysRequest:
    out: ListPublicKeysRequest = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import capo_cloudtrail.types.date

        out["start_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_cloudtrail.types.date

        out["end_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
