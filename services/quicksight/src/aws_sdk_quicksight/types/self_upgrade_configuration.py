"""Generated from Smithy shape ``com.amazonaws.quicksight#SelfUpgradeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.self_upgrade_status


class SelfUpgradeConfiguration(TypedDict):
    self_upgrade_status: NotRequired[
        "aws_sdk_quicksight.types.self_upgrade_status.SelfUpgradeStatus"
    ]
    """<p>Status set for the self-upgrade configuration for the Quick account. It can contain the following values:</p> <ul> <li> <p> <code>AUTO_APPROVAL</code>: All the self-upgrade requests will be auto approved.</p> </li> <li> <p> <code>ADMIN_APPROVAL</code>: All the self-upgrade requests will require admin approval.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfUpgradeConfiguration) -> dict:
    out: dict = {}
    if "self_upgrade_status" in value:
        import aws_sdk_quicksight.types.self_upgrade_status

        out["SelfUpgradeStatus"] = (
            aws_sdk_quicksight.types.self_upgrade_status.serialize_json(
                value["self_upgrade_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelfUpgradeConfiguration:
    out: SelfUpgradeConfiguration = {}  # type: ignore[typeddict-item]
    if "SelfUpgradeStatus" in data:
        import aws_sdk_quicksight.types.self_upgrade_status

        out["self_upgrade_status"] = (
            aws_sdk_quicksight.types.self_upgrade_status.deserialize_json(
                data["SelfUpgradeStatus"]
            )
        )
    return out
