"""Generated from Smithy shape ``com.amazonaws.batch#UpdateQuotaShareResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class UpdateQuotaShareResponse(TypedDict):
    quota_share_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the quota share.</p>"""
    quota_share_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the quota share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuotaShareResponse) -> dict:
    out: dict = {}
    if "quota_share_name" in value:
        out["quotaShareName"] = value["quota_share_name"]
    if "quota_share_arn" in value:
        out["quotaShareArn"] = value["quota_share_arn"]
    return out


def deserialize_json(data: dict) -> UpdateQuotaShareResponse:
    out: UpdateQuotaShareResponse = {}  # type: ignore[typeddict-item]
    if "quotaShareName" in data:
        out["quota_share_name"] = data["quotaShareName"]
    if "quotaShareArn" in data:
        out["quota_share_arn"] = data["quotaShareArn"]
    return out
