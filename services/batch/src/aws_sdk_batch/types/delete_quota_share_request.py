"""Generated from Smithy shape ``com.amazonaws.batch#DeleteQuotaShareRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class DeleteQuotaShareRequest(TypedDict):
    quota_share_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the quota share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQuotaShareRequest) -> dict:
    out: dict = {}
    if "quota_share_arn" in value:
        out["quotaShareArn"] = value["quota_share_arn"]
    return out


def deserialize_json(data: dict) -> DeleteQuotaShareRequest:
    out: DeleteQuotaShareRequest = {}  # type: ignore[typeddict-item]
    if "quotaShareArn" in data:
        out["quota_share_arn"] = data["quotaShareArn"]
    return out
