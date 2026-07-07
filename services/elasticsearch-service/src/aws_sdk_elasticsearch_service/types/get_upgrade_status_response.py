"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#GetUpgradeStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.upgrade_name
    import aws_sdk_elasticsearch_service.types.upgrade_status
    import aws_sdk_elasticsearch_service.types.upgrade_step


class GetUpgradeStatusResponse(TypedDict, closed=True):
    upgrade_step: NotRequired[
        "aws_sdk_elasticsearch_service.types.upgrade_step.UpgradeStep"
    ]
    """<p> Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through: <ul> <li>PreUpgradeCheck</li> <li>Snapshot</li> <li>Upgrade</li> </ul> </p>"""
    step_status: NotRequired[
        "aws_sdk_elasticsearch_service.types.upgrade_status.UpgradeStatus"
    ]
    """<p> One of 4 statuses that a step can go through returned as part of the <code> <a>GetUpgradeStatusResponse</a> </code> object. The status can take one of the following values: <ul> <li>In Progress</li> <li>Succeeded</li> <li>Succeeded with Issues</li> <li>Failed</li> </ul> </p>"""
    upgrade_name: NotRequired[
        "aws_sdk_elasticsearch_service.types.upgrade_name.UpgradeName"
    ]
    """<p>A string that describes the update briefly</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUpgradeStatusResponse) -> dict:
    out: dict = {}
    if "upgrade_step" in value:
        import aws_sdk_elasticsearch_service.types.upgrade_step

        out["UpgradeStep"] = (
            aws_sdk_elasticsearch_service.types.upgrade_step.serialize_json(
                value["upgrade_step"]
            )
        )
    if "step_status" in value:
        import aws_sdk_elasticsearch_service.types.upgrade_status

        out["StepStatus"] = (
            aws_sdk_elasticsearch_service.types.upgrade_status.serialize_json(
                value["step_status"]
            )
        )
    if "upgrade_name" in value:
        out["UpgradeName"] = value["upgrade_name"]
    return out


def deserialize_json(data: dict) -> GetUpgradeStatusResponse:
    out: GetUpgradeStatusResponse = {}  # type: ignore[typeddict-item]
    if "UpgradeStep" in data:
        import aws_sdk_elasticsearch_service.types.upgrade_step

        out["upgrade_step"] = (
            aws_sdk_elasticsearch_service.types.upgrade_step.deserialize_json(
                data["UpgradeStep"]
            )
        )
    if "StepStatus" in data:
        import aws_sdk_elasticsearch_service.types.upgrade_status

        out["step_status"] = (
            aws_sdk_elasticsearch_service.types.upgrade_status.deserialize_json(
                data["StepStatus"]
            )
        )
    if "UpgradeName" in data:
        out["upgrade_name"] = data["UpgradeName"]
    return out
