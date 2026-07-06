"""Generated from Smithy shape ``com.amazonaws.batch#CreateSchedulingPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.fairshare_policy
    import aws_sdk_batch.types.quota_share_policy
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class CreateSchedulingPolicyRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the fair-share scheduling policy. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>"""
    quota_share_policy: NotRequired[
        "aws_sdk_batch.types.quota_share_policy.QuotaSharePolicy"
    ]
    """<p>The quota share scheduling policy details. Only one of fairsharePolicy or quotaSharePolicy can be set. Once set, this policy type cannot be removed or changed to a fairSharePolicy.</p>"""
    fairshare_policy: NotRequired[
        "aws_sdk_batch.types.fairshare_policy.FairsharePolicy"
    ]
    """<p>The fair-share scheduling policy details. Only one of fairsharePolicy or quotaSharePolicy can be set. Once set, this policy type cannot be removed or changed to a quotaSharePolicy.</p>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    r"""<p>The tags that you apply to the scheduling policy to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a> in <i>Amazon Web Services General Reference</i>.</p> <p>These tags can be updated or removed using the <a href=\"https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html\">TagResource</a> and <a href=\"https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html\">UntagResource</a> API operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSchedulingPolicyRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
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
    if "tags" in value:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSchedulingPolicyRequest:
    out: CreateSchedulingPolicyRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
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
    if "tags" in data:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    return out
