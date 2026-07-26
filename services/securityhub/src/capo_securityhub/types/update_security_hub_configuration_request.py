"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateSecurityHubConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.control_finding_generator


class UpdateSecurityHubConfigurationRequest(TypedDict, closed=True):
    auto_enable_controls: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether to automatically enable new controls when they are added to standards that are enabled.</p> <p>By default, this is set to <code>true</code>, and new controls are enabled automatically. To not automatically enable new controls, set this to <code>false</code>. </p> <p>When you automatically enable new controls, you can interact with the controls in the console and programmatically immediately after release. However, automatically enabled controls have a temporary default status of <code>DISABLED</code>. It can take up to several days for Security Hub CSPM to process the control release and designate the control as <code>ENABLED</code> in your account. During the processing period, you can manually enable or disable a control, and Security Hub CSPM will maintain that designation regardless of whether you have <code>AutoEnableControls</code> set to <code>true</code>.</p>"""
    control_finding_generator: NotRequired[
        "capo_securityhub.types.control_finding_generator.ControlFindingGenerator"
    ]
    """<p>Updates whether the calling account has consolidated control findings turned on. If the value for this field is set to <code>SECURITY_CONTROL</code>, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.</p> <p>If the value for this field is set to <code>STANDARD_CONTROL</code>, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.</p> <p>For accounts that are part of an organization, this value can only be updated in the administrator account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSecurityHubConfigurationRequest) -> dict:
    out: dict = {}
    if "auto_enable_controls" in value:
        out["AutoEnableControls"] = value["auto_enable_controls"]
    if "control_finding_generator" in value:
        import capo_securityhub.types.control_finding_generator

        out["ControlFindingGenerator"] = (
            capo_securityhub.types.control_finding_generator.serialize_json(
                value["control_finding_generator"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSecurityHubConfigurationRequest:
    out: UpdateSecurityHubConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "AutoEnableControls" in data:
        out["auto_enable_controls"] = data["AutoEnableControls"]
    if "ControlFindingGenerator" in data:
        import capo_securityhub.types.control_finding_generator

        out["control_finding_generator"] = (
            capo_securityhub.types.control_finding_generator.deserialize_json(
                data["ControlFindingGenerator"]
            )
        )
    return out
