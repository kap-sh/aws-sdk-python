"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSelfUpgradeConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.self_upgrade_status


class UpdateSelfUpgradeConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the Quick self-upgrade configuration that you want to update.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The Quick namespace that you want to update the Quick self-upgrade configuration for.</p>"""
    self_upgrade_status: (
        "aws_sdk_quicksight.types.self_upgrade_status.SelfUpgradeStatus"
    )
    """<p>The self-upgrade status that you want to set for the Quick account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSelfUpgradeConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.self_upgrade_status

    out["SelfUpgradeStatus"] = (
        aws_sdk_quicksight.types.self_upgrade_status.serialize_json(
            value["self_upgrade_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateSelfUpgradeConfigurationRequest:
    out: UpdateSelfUpgradeConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "SelfUpgradeStatus" in data:
        import aws_sdk_quicksight.types.self_upgrade_status

        out["self_upgrade_status"] = (
            aws_sdk_quicksight.types.self_upgrade_status.deserialize_json(
                data["SelfUpgradeStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSelfUpgradeConfigurationRequest.self_upgrade_status required"
        )
    return out
