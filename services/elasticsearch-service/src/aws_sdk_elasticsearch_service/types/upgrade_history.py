"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpgradeHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.start_timestamp
    import aws_sdk_elasticsearch_service.types.upgrade_name
    import aws_sdk_elasticsearch_service.types.upgrade_status
    import aws_sdk_elasticsearch_service.types.upgrade_steps_list


class UpgradeHistory(TypedDict, closed=True):
    upgrade_name: NotRequired[
        "aws_sdk_elasticsearch_service.types.upgrade_name.UpgradeName"
    ]
    """<p>A string that describes the update briefly</p>"""
    start_timestamp: NotRequired[
        "aws_sdk_elasticsearch_service.types.start_timestamp.StartTimestamp"
    ]
    r"""<p>UTC Timestamp at which the Upgrade API call was made in \"yyyy-MM-ddTHH:mm:ssZ\" format.</p>"""
    upgrade_status: NotRequired[
        "aws_sdk_elasticsearch_service.types.upgrade_status.UpgradeStatus"
    ]
    """<p> The overall status of the update. The status can take one of the following values: <ul> <li>In Progress</li> <li>Succeeded</li> <li>Succeeded with Issues</li> <li>Failed</li> </ul> </p>"""
    steps_list: NotRequired[
        "aws_sdk_elasticsearch_service.types.upgrade_steps_list.UpgradeStepsList"
    ]
    """<p> A list of <code> <a>UpgradeStepItem</a> </code> s representing information about each step performed as pard of a specific Upgrade or Upgrade Eligibility Check. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeHistory) -> dict:
    out: dict = {}
    if "upgrade_name" in value:
        out["UpgradeName"] = value["upgrade_name"]
    if "start_timestamp" in value:
        import aws_sdk_elasticsearch_service.types.start_timestamp

        out["StartTimestamp"] = (
            aws_sdk_elasticsearch_service.types.start_timestamp.serialize_json(
                value["start_timestamp"]
            )
        )
    if "upgrade_status" in value:
        import aws_sdk_elasticsearch_service.types.upgrade_status

        out["UpgradeStatus"] = (
            aws_sdk_elasticsearch_service.types.upgrade_status.serialize_json(
                value["upgrade_status"]
            )
        )
    if "steps_list" in value:
        import aws_sdk_elasticsearch_service.types.upgrade_steps_list

        out["StepsList"] = (
            aws_sdk_elasticsearch_service.types.upgrade_steps_list.serialize_json(
                value["steps_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpgradeHistory:
    out: UpgradeHistory = {}  # type: ignore[typeddict-item]
    if "UpgradeName" in data:
        out["upgrade_name"] = data["UpgradeName"]
    if "StartTimestamp" in data:
        import aws_sdk_elasticsearch_service.types.start_timestamp

        out["start_timestamp"] = (
            aws_sdk_elasticsearch_service.types.start_timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    if "UpgradeStatus" in data:
        import aws_sdk_elasticsearch_service.types.upgrade_status

        out["upgrade_status"] = (
            aws_sdk_elasticsearch_service.types.upgrade_status.deserialize_json(
                data["UpgradeStatus"]
            )
        )
    if "StepsList" in data:
        import aws_sdk_elasticsearch_service.types.upgrade_steps_list

        out["steps_list"] = (
            aws_sdk_elasticsearch_service.types.upgrade_steps_list.deserialize_json(
                data["StepsList"]
            )
        )
    return out
