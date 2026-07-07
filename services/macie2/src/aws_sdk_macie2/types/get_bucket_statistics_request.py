"""Generated from Smithy shape ``com.amazonaws.macie2#GetBucketStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class GetBucketStatisticsRequest(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBucketStatisticsRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> GetBucketStatisticsRequest:
    out: GetBucketStatisticsRequest = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    return out
