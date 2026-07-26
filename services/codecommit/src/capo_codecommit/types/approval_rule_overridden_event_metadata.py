"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalRuleOverriddenEventMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.override_status
    import capo_codecommit.types.revision_id


class ApprovalRuleOverriddenEventMetadata(TypedDict, closed=True):
    revision_id: NotRequired["capo_codecommit.types.revision_id.RevisionId"]
    """<p>The revision ID of the pull request when the override event occurred.</p>"""
    override_status: NotRequired["capo_codecommit.types.override_status.OverrideStatus"]
    """<p>The status of the override event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalRuleOverriddenEventMetadata) -> dict:
    out: dict = {}
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "override_status" in value:
        import capo_codecommit.types.override_status

        out["overrideStatus"] = (
            capo_codecommit.types.override_status.serialize_aws_json_1_1(
                value["override_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApprovalRuleOverriddenEventMetadata:
    out: ApprovalRuleOverriddenEventMetadata = {}  # type: ignore[typeddict-item]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    if "overrideStatus" in data:
        import capo_codecommit.types.override_status

        out["override_status"] = (
            capo_codecommit.types.override_status.deserialize_aws_json_1_1(
                data["overrideStatus"]
            )
        )
    return out
