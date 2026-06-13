"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeSelfUpgradeConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.self_upgrade_configuration
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeSelfUpgradeConfigurationResponse(TypedDict):
    self_upgrade_configuration: NotRequired[
        "aws_sdk_quicksight.types.self_upgrade_configuration.SelfUpgradeConfiguration"
    ]
    """<p>The self-upgrade configuration for the Quick account.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSelfUpgradeConfigurationResponse) -> dict:
    out: dict = {}
    if "self_upgrade_configuration" in value:
        import aws_sdk_quicksight.types.self_upgrade_configuration

        out["SelfUpgradeConfiguration"] = (
            aws_sdk_quicksight.types.self_upgrade_configuration.serialize_json(
                value["self_upgrade_configuration"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeSelfUpgradeConfigurationResponse:
    out: DescribeSelfUpgradeConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "SelfUpgradeConfiguration" in data:
        import aws_sdk_quicksight.types.self_upgrade_configuration

        out["self_upgrade_configuration"] = (
            aws_sdk_quicksight.types.self_upgrade_configuration.deserialize_json(
                data["SelfUpgradeConfiguration"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
