"""Generated from Smithy shape ``com.amazonaws.opensearch#GetUpgradeStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.upgrade_name
    import capo_opensearch.types.upgrade_status
    import capo_opensearch.types.upgrade_step


class GetUpgradeStatusResponse(TypedDict, closed=True):
    upgrade_step: NotRequired["capo_opensearch.types.upgrade_step.UpgradeStep"]
    """<p>One of three steps that an upgrade or upgrade eligibility check goes through.</p>"""
    step_status: NotRequired["capo_opensearch.types.upgrade_status.UpgradeStatus"]
    """<p>The status of the current step that an upgrade is on.</p>"""
    upgrade_name: NotRequired["capo_opensearch.types.upgrade_name.UpgradeName"]
    """<p>A string that describes the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUpgradeStatusResponse) -> dict:
    out: dict = {}
    if "upgrade_step" in value:
        import capo_opensearch.types.upgrade_step

        out["UpgradeStep"] = capo_opensearch.types.upgrade_step.serialize_json(
            value["upgrade_step"]
        )
    if "step_status" in value:
        import capo_opensearch.types.upgrade_status

        out["StepStatus"] = capo_opensearch.types.upgrade_status.serialize_json(
            value["step_status"]
        )
    if "upgrade_name" in value:
        out["UpgradeName"] = value["upgrade_name"]
    return out


def deserialize_json(data: dict) -> GetUpgradeStatusResponse:
    out: GetUpgradeStatusResponse = {}  # type: ignore[typeddict-item]
    if "UpgradeStep" in data:
        import capo_opensearch.types.upgrade_step

        out["upgrade_step"] = capo_opensearch.types.upgrade_step.deserialize_json(
            data["UpgradeStep"]
        )
    if "StepStatus" in data:
        import capo_opensearch.types.upgrade_status

        out["step_status"] = capo_opensearch.types.upgrade_status.deserialize_json(
            data["StepStatus"]
        )
    if "UpgradeName" in data:
        out["upgrade_name"] = data["UpgradeName"]
    return out
