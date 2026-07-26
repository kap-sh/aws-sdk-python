"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpgradeStepItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.double
    import capo_elasticsearch_service.types.issues
    import capo_elasticsearch_service.types.upgrade_status
    import capo_elasticsearch_service.types.upgrade_step


class UpgradeStepItem(TypedDict, closed=True):
    upgrade_step: NotRequired[
        "capo_elasticsearch_service.types.upgrade_step.UpgradeStep"
    ]
    """<p> Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through: <ul> <li>PreUpgradeCheck</li> <li>Snapshot</li> <li>Upgrade</li> </ul> </p>"""
    upgrade_step_status: NotRequired[
        "capo_elasticsearch_service.types.upgrade_status.UpgradeStatus"
    ]
    """<p> The status of a particular step during an upgrade. The status can take one of the following values: <ul> <li>In Progress</li> <li>Succeeded</li> <li>Succeeded with Issues</li> <li>Failed</li> </ul> </p>"""
    issues: NotRequired["capo_elasticsearch_service.types.issues.Issues"]
    """<p>A list of strings containing detailed information about the errors encountered in a particular step.</p>"""
    progress_percent: NotRequired["capo_elasticsearch_service.types.double.Double"]
    """<p>The Floating point value representing progress percentage of a particular step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeStepItem) -> dict:
    out: dict = {}
    if "upgrade_step" in value:
        import capo_elasticsearch_service.types.upgrade_step

        out["UpgradeStep"] = (
            capo_elasticsearch_service.types.upgrade_step.serialize_json(
                value["upgrade_step"]
            )
        )
    if "upgrade_step_status" in value:
        import capo_elasticsearch_service.types.upgrade_status

        out["UpgradeStepStatus"] = (
            capo_elasticsearch_service.types.upgrade_status.serialize_json(
                value["upgrade_step_status"]
            )
        )
    if "issues" in value:
        import capo_elasticsearch_service.types.issues

        out["Issues"] = capo_elasticsearch_service.types.issues.serialize_json(
            value["issues"]
        )
    if "progress_percent" in value:
        out["ProgressPercent"] = value["progress_percent"]
    return out


def deserialize_json(data: dict) -> UpgradeStepItem:
    out: UpgradeStepItem = {}  # type: ignore[typeddict-item]
    if "UpgradeStep" in data:
        import capo_elasticsearch_service.types.upgrade_step

        out["upgrade_step"] = (
            capo_elasticsearch_service.types.upgrade_step.deserialize_json(
                data["UpgradeStep"]
            )
        )
    if "UpgradeStepStatus" in data:
        import capo_elasticsearch_service.types.upgrade_status

        out["upgrade_step_status"] = (
            capo_elasticsearch_service.types.upgrade_status.deserialize_json(
                data["UpgradeStepStatus"]
            )
        )
    if "Issues" in data:
        import capo_elasticsearch_service.types.issues

        out["issues"] = capo_elasticsearch_service.types.issues.deserialize_json(
            data["Issues"]
        )
    if "ProgressPercent" in data:
        out["progress_percent"] = data["ProgressPercent"]
    return out
