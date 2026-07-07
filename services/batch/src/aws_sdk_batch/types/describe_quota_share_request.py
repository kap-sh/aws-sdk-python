"""Generated from Smithy shape ``com.amazonaws.batch#DescribeQuotaShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class DescribeQuotaShareRequest(TypedDict, closed=True):
    quota_share_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the quota share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQuotaShareRequest) -> dict:
    out: dict = {}
    if "quota_share_arn" in value:
        out["quotaShareArn"] = value["quota_share_arn"]
    return out


def deserialize_json(data: dict) -> DescribeQuotaShareRequest:
    out: DescribeQuotaShareRequest = {}  # type: ignore[typeddict-item]
    if "quotaShareArn" in data:
        out["quota_share_arn"] = data["quotaShareArn"]
    return out
