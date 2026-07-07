"""Generated from Smithy shape ``com.amazonaws.opensearch#UpgradeHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.start_timestamp
    import aws_sdk_opensearch.types.upgrade_name
    import aws_sdk_opensearch.types.upgrade_status
    import aws_sdk_opensearch.types.upgrade_steps_list


class UpgradeHistory(TypedDict, closed=True):
    upgrade_name: NotRequired["aws_sdk_opensearch.types.upgrade_name.UpgradeName"]
    """<p>A string that describes the upgrade.</p>"""
    start_timestamp: NotRequired[
        "aws_sdk_opensearch.types.start_timestamp.StartTimestamp"
    ]
    """<p>UTC timestamp at which the upgrade API call was made, in the format <code>yyyy-MM-ddTHH:mm:ssZ</code>.</p>"""
    upgrade_status: NotRequired["aws_sdk_opensearch.types.upgrade_status.UpgradeStatus"]
    """<p> The current status of the upgrade. The status can take one of the following values: </p> <ul> <li> <p>In Progress</p> </li> <li> <p>Succeeded</p> </li> <li> <p>Succeeded with Issues</p> </li> <li> <p>Failed</p> </li> </ul>"""
    steps_list: NotRequired[
        "aws_sdk_opensearch.types.upgrade_steps_list.UpgradeStepsList"
    ]
    """<p>A list of each step performed as part of a specific upgrade or upgrade eligibility check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeHistory) -> dict:
    out: dict = {}
    if "upgrade_name" in value:
        out["UpgradeName"] = value["upgrade_name"]
    if "start_timestamp" in value:
        import aws_sdk_opensearch.types.start_timestamp

        out["StartTimestamp"] = aws_sdk_opensearch.types.start_timestamp.serialize_json(
            value["start_timestamp"]
        )
    if "upgrade_status" in value:
        import aws_sdk_opensearch.types.upgrade_status

        out["UpgradeStatus"] = aws_sdk_opensearch.types.upgrade_status.serialize_json(
            value["upgrade_status"]
        )
    if "steps_list" in value:
        import aws_sdk_opensearch.types.upgrade_steps_list

        out["StepsList"] = aws_sdk_opensearch.types.upgrade_steps_list.serialize_json(
            value["steps_list"]
        )
    return out


def deserialize_json(data: dict) -> UpgradeHistory:
    out: UpgradeHistory = {}  # type: ignore[typeddict-item]
    if "UpgradeName" in data:
        out["upgrade_name"] = data["UpgradeName"]
    if "StartTimestamp" in data:
        import aws_sdk_opensearch.types.start_timestamp

        out["start_timestamp"] = (
            aws_sdk_opensearch.types.start_timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    if "UpgradeStatus" in data:
        import aws_sdk_opensearch.types.upgrade_status

        out["upgrade_status"] = (
            aws_sdk_opensearch.types.upgrade_status.deserialize_json(
                data["UpgradeStatus"]
            )
        )
    if "StepsList" in data:
        import aws_sdk_opensearch.types.upgrade_steps_list

        out["steps_list"] = (
            aws_sdk_opensearch.types.upgrade_steps_list.deserialize_json(
                data["StepsList"]
            )
        )
    return out
