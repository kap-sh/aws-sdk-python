"""Generated from Smithy shape ``com.amazonaws.opensearch#UpgradeStepItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.double
    import capo_opensearch.types.issues
    import capo_opensearch.types.upgrade_status
    import capo_opensearch.types.upgrade_step


class UpgradeStepItem(TypedDict, closed=True):
    upgrade_step: NotRequired["capo_opensearch.types.upgrade_step.UpgradeStep"]
    """<p> One of three steps that an upgrade or upgrade eligibility check goes through: </p> <ul> <li> <p>PreUpgradeCheck</p> </li> <li> <p>Snapshot</p> </li> <li> <p>Upgrade</p> </li> </ul>"""
    upgrade_step_status: NotRequired[
        "capo_opensearch.types.upgrade_status.UpgradeStatus"
    ]
    """<p> The current status of the upgrade. The status can take one of the following values: </p> <ul> <li> <p>In Progress</p> </li> <li> <p>Succeeded</p> </li> <li> <p>Succeeded with Issues</p> </li> <li> <p>Failed</p> </li> </ul>"""
    issues: NotRequired["capo_opensearch.types.issues.Issues"]
    """<p>A list of strings containing detailed information about the errors encountered in a particular step.</p>"""
    progress_percent: NotRequired["capo_opensearch.types.double.Double"]
    """<p>The floating point value representing the progress percentage of a particular step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeStepItem) -> dict:
    out: dict = {}
    if "upgrade_step" in value:
        import capo_opensearch.types.upgrade_step

        out["UpgradeStep"] = capo_opensearch.types.upgrade_step.serialize_json(
            value["upgrade_step"]
        )
    if "upgrade_step_status" in value:
        import capo_opensearch.types.upgrade_status

        out["UpgradeStepStatus"] = capo_opensearch.types.upgrade_status.serialize_json(
            value["upgrade_step_status"]
        )
    if "issues" in value:
        import capo_opensearch.types.issues

        out["Issues"] = capo_opensearch.types.issues.serialize_json(value["issues"])
    if "progress_percent" in value:
        out["ProgressPercent"] = value["progress_percent"]
    return out


def deserialize_json(data: dict) -> UpgradeStepItem:
    out: UpgradeStepItem = {}  # type: ignore[typeddict-item]
    if "UpgradeStep" in data:
        import capo_opensearch.types.upgrade_step

        out["upgrade_step"] = capo_opensearch.types.upgrade_step.deserialize_json(
            data["UpgradeStep"]
        )
    if "UpgradeStepStatus" in data:
        import capo_opensearch.types.upgrade_status

        out["upgrade_step_status"] = (
            capo_opensearch.types.upgrade_status.deserialize_json(
                data["UpgradeStepStatus"]
            )
        )
    if "Issues" in data:
        import capo_opensearch.types.issues

        out["issues"] = capo_opensearch.types.issues.deserialize_json(data["Issues"])
    if "ProgressPercent" in data:
        out["progress_percent"] = data["ProgressPercent"]
    return out
