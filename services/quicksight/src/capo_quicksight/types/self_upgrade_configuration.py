"""Generated from Smithy shape ``com.amazonaws.quicksight#SelfUpgradeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.self_upgrade_status


class SelfUpgradeConfiguration(TypedDict, closed=True):
    self_upgrade_status: NotRequired[
        "capo_quicksight.types.self_upgrade_status.SelfUpgradeStatus"
    ]
    """<p>Status set for the self-upgrade configuration for the Quick account. It can contain the following values:</p> <ul> <li> <p> <code>AUTO_APPROVAL</code>: All the self-upgrade requests will be auto approved.</p> </li> <li> <p> <code>ADMIN_APPROVAL</code>: All the self-upgrade requests will require admin approval.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfUpgradeConfiguration) -> dict:
    out: dict = {}
    if "self_upgrade_status" in value:
        import capo_quicksight.types.self_upgrade_status

        out["SelfUpgradeStatus"] = (
            capo_quicksight.types.self_upgrade_status.serialize_json(
                value["self_upgrade_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelfUpgradeConfiguration:
    out: SelfUpgradeConfiguration = {}  # type: ignore[typeddict-item]
    if "SelfUpgradeStatus" in data:
        import capo_quicksight.types.self_upgrade_status

        out["self_upgrade_status"] = (
            capo_quicksight.types.self_upgrade_status.deserialize_json(
                data["SelfUpgradeStatus"]
            )
        )
    return out
