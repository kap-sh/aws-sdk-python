"""Generated from Smithy shape ``com.amazonaws.codepipeline#TransitionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.disabled_reason
    import capo_codepipeline.types.enabled
    import capo_codepipeline.types.last_changed_at
    import capo_codepipeline.types.last_changed_by


class TransitionState(TypedDict, closed=True):
    enabled: "capo_codepipeline.types.enabled.Enabled"
    """<p>Whether the transition between stages is enabled (true) or disabled (false).</p>"""
    last_changed_by: NotRequired[
        "capo_codepipeline.types.last_changed_by.LastChangedBy"
    ]
    """<p>The ID of the user who last changed the transition state.</p>"""
    last_changed_at: NotRequired[
        "capo_codepipeline.types.last_changed_at.LastChangedAt"
    ]
    """<p>The timestamp when the transition state was last changed.</p>"""
    disabled_reason: NotRequired[
        "capo_codepipeline.types.disabled_reason.DisabledReason"
    ]
    """<p>The user-specified reason why the transition between two stages of a pipeline was disabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransitionState) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "last_changed_by" in value:
        out["lastChangedBy"] = value["last_changed_by"]
    if "last_changed_at" in value:
        import capo_codepipeline.types.last_changed_at

        out["lastChangedAt"] = (
            capo_codepipeline.types.last_changed_at.serialize_aws_json_1_1(
                value["last_changed_at"]
            )
        )
    if "disabled_reason" in value:
        out["disabledReason"] = value["disabled_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransitionState:
    out: TransitionState = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "lastChangedBy" in data:
        out["last_changed_by"] = data["lastChangedBy"]
    if "lastChangedAt" in data:
        import capo_codepipeline.types.last_changed_at

        out["last_changed_at"] = (
            capo_codepipeline.types.last_changed_at.deserialize_aws_json_1_1(
                data["lastChangedAt"]
            )
        )
    if "disabledReason" in data:
        out["disabled_reason"] = data["disabledReason"]
    return out
