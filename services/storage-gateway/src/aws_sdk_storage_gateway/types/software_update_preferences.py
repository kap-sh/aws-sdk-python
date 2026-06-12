"""Generated from Smithy shape ``com.amazonaws.storagegateway#SoftwareUpdatePreferences``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.automatic_update_policy


class SoftwareUpdatePreferences(TypedDict):
    automatic_update_policy: NotRequired[
        "aws_sdk_storage_gateway.types.automatic_update_policy.AutomaticUpdatePolicy"
    ]
    """<p>Indicates the automatic update policy for a gateway.</p> <p> <code>ALL_VERSIONS</code> - Enables regular gateway maintenance updates.</p> <p> <code>EMERGENCY_VERSIONS_ONLY</code> - Disables regular gateway maintenance updates. The gateway will still receive emergency version updates on rare occasions if necessary to remedy highly critical security or durability issues. You will be notified before an emergency version update is applied. These updates are applied during your gateway's scheduled maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SoftwareUpdatePreferences) -> dict:
    out: dict = {}
    if "automatic_update_policy" in value:
        import aws_sdk_storage_gateway.types.automatic_update_policy

        out["AutomaticUpdatePolicy"] = (
            aws_sdk_storage_gateway.types.automatic_update_policy.serialize_aws_json_1_1(
                value["automatic_update_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SoftwareUpdatePreferences:
    out: SoftwareUpdatePreferences = {}  # type: ignore[typeddict-item]
    if "AutomaticUpdatePolicy" in data:
        import aws_sdk_storage_gateway.types.automatic_update_policy

        out["automatic_update_policy"] = (
            aws_sdk_storage_gateway.types.automatic_update_policy.deserialize_aws_json_1_1(
                data["AutomaticUpdatePolicy"]
            )
        )
    return out
