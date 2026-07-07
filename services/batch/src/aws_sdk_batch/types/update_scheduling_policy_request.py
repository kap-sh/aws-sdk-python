"""Generated from Smithy shape ``com.amazonaws.batch#UpdateSchedulingPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.fairshare_policy
    import aws_sdk_batch.types.quota_share_policy
    import aws_sdk_batch.types.string


class UpdateSchedulingPolicyRequest(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the scheduling policy to update.</p>"""
    quota_share_policy: NotRequired[
        "aws_sdk_batch.types.quota_share_policy.QuotaSharePolicy"
    ]
    """<p>The quota share scheduling policy details. Once set during creation, a quotaSharePolicy cannot be removed or changed to a fairsharePolicy.</p>"""
    fairshare_policy: NotRequired[
        "aws_sdk_batch.types.fairshare_policy.FairsharePolicy"
    ]
    """<p>The fair-share policy scheduling details. Once set during creation, a fairsharePolicy cannot be removed or changed to a quotaSharePolicy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSchedulingPolicyRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "quota_share_policy" in value:
        import aws_sdk_batch.types.quota_share_policy

        out["quotaSharePolicy"] = aws_sdk_batch.types.quota_share_policy.serialize_json(
            value["quota_share_policy"]
        )
    if "fairshare_policy" in value:
        import aws_sdk_batch.types.fairshare_policy

        out["fairsharePolicy"] = aws_sdk_batch.types.fairshare_policy.serialize_json(
            value["fairshare_policy"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSchedulingPolicyRequest:
    out: UpdateSchedulingPolicyRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "quotaSharePolicy" in data:
        import aws_sdk_batch.types.quota_share_policy

        out["quota_share_policy"] = (
            aws_sdk_batch.types.quota_share_policy.deserialize_json(
                data["quotaSharePolicy"]
            )
        )
    if "fairsharePolicy" in data:
        import aws_sdk_batch.types.fairshare_policy

        out["fairshare_policy"] = aws_sdk_batch.types.fairshare_policy.deserialize_json(
            data["fairsharePolicy"]
        )
    return out
