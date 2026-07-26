"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.account_targeting
    import capo_fis.types.actions_mode
    import capo_fis.types.empty_target_resolution_mode


class ExperimentOptions(TypedDict, closed=True):
    account_targeting: NotRequired["capo_fis.types.account_targeting.AccountTargeting"]
    """<p>The account targeting setting for an experiment.</p>"""
    empty_target_resolution_mode: NotRequired[
        "capo_fis.types.empty_target_resolution_mode.EmptyTargetResolutionMode"
    ]
    """<p>The empty target resolution mode for an experiment.</p>"""
    actions_mode: NotRequired["capo_fis.types.actions_mode.ActionsMode"]
    """<p>The actions mode of the experiment that is set from the StartExperiment API command.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentOptions) -> dict:
    out: dict = {}
    if "account_targeting" in value:
        import capo_fis.types.account_targeting

        out["accountTargeting"] = capo_fis.types.account_targeting.serialize_json(
            value["account_targeting"]
        )
    if "empty_target_resolution_mode" in value:
        import capo_fis.types.empty_target_resolution_mode

        out["emptyTargetResolutionMode"] = (
            capo_fis.types.empty_target_resolution_mode.serialize_json(
                value["empty_target_resolution_mode"]
            )
        )
    if "actions_mode" in value:
        import capo_fis.types.actions_mode

        out["actionsMode"] = capo_fis.types.actions_mode.serialize_json(
            value["actions_mode"]
        )
    return out


def deserialize_json(data: dict) -> ExperimentOptions:
    out: ExperimentOptions = {}  # type: ignore[typeddict-item]
    if "accountTargeting" in data:
        import capo_fis.types.account_targeting

        out["account_targeting"] = capo_fis.types.account_targeting.deserialize_json(
            data["accountTargeting"]
        )
    if "emptyTargetResolutionMode" in data:
        import capo_fis.types.empty_target_resolution_mode

        out["empty_target_resolution_mode"] = (
            capo_fis.types.empty_target_resolution_mode.deserialize_json(
                data["emptyTargetResolutionMode"]
            )
        )
    if "actionsMode" in data:
        import capo_fis.types.actions_mode

        out["actions_mode"] = capo_fis.types.actions_mode.deserialize_json(
            data["actionsMode"]
        )
    return out
