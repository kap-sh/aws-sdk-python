"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateAutomatedDiscoveryConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.auto_enable_mode
    import aws_sdk_macie2.types.automated_discovery_status


class UpdateAutomatedDiscoveryConfigurationRequest(TypedDict):
    auto_enable_organization_members: NotRequired[
        "aws_sdk_macie2.types.auto_enable_mode.AutoEnableMode"
    ]
    """<p>Specifies whether to automatically enable automated sensitive data discovery for accounts in the organization. Valid values are: ALL (default), enable it for all existing accounts and new member accounts; NEW, enable it only for new member accounts; and, NONE, don't enable it for any accounts.</p> <p>If you specify NEW or NONE, automated sensitive data discovery continues to be enabled for any existing accounts that it's currently enabled for. To enable or disable it for individual member accounts, specify NEW or NONE, and then enable or disable it for each account by using the BatchUpdateAutomatedDiscoveryAccounts operation.</p>"""
    status: NotRequired[
        "aws_sdk_macie2.types.automated_discovery_status.AutomatedDiscoveryStatus"
    ]
    """<p>The new status of automated sensitive data discovery for the organization or account. Valid values are: ENABLED, start or resume all automated sensitive data discovery activities; and, DISABLED, stop performing all automated sensitive data discovery activities.</p> <p>If you specify DISABLED for an administrator account, you also disable automated sensitive data discovery for all member accounts in the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomatedDiscoveryConfigurationRequest) -> dict:
    out: dict = {}
    if "auto_enable_organization_members" in value:
        import aws_sdk_macie2.types.auto_enable_mode

        out["autoEnableOrganizationMembers"] = (
            aws_sdk_macie2.types.auto_enable_mode.serialize_json(
                value["auto_enable_organization_members"]
            )
        )
    if "status" in value:
        import aws_sdk_macie2.types.automated_discovery_status

        out["status"] = aws_sdk_macie2.types.automated_discovery_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAutomatedDiscoveryConfigurationRequest:
    out: UpdateAutomatedDiscoveryConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "autoEnableOrganizationMembers" in data:
        import aws_sdk_macie2.types.auto_enable_mode

        out["auto_enable_organization_members"] = (
            aws_sdk_macie2.types.auto_enable_mode.deserialize_json(
                data["autoEnableOrganizationMembers"]
            )
        )
    if "status" in data:
        import aws_sdk_macie2.types.automated_discovery_status

        out["status"] = (
            aws_sdk_macie2.types.automated_discovery_status.deserialize_json(
                data["status"]
            )
        )
    return out
