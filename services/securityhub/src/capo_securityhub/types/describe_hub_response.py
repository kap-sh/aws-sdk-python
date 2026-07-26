"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeHubResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.control_finding_generator
    import capo_securityhub.types.non_empty_string


class DescribeHubResponse(TypedDict, closed=True):
    hub_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the Hub resource that was retrieved.</p>"""
    subscribed_at: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The date and time when Security Hub CSPM was enabled in the account.</p>"""
    auto_enable_controls: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether to automatically enable new controls when they are added to standards that are enabled.</p> <p>If set to <code>true</code>, then new controls for enabled standards are enabled automatically. If set to <code>false</code>, then new controls are not enabled.</p> <p>When you automatically enable new controls, you can interact with the controls in the console and programmatically immediately after release. However, automatically enabled controls have a temporary default status of <code>DISABLED</code>. It can take up to several days for Security Hub CSPM to process the control release and designate the control as <code>ENABLED</code> in your account. During the processing period, you can manually enable or disable a control, and Security Hub CSPM will maintain that designation regardless of whether you have <code>AutoEnableControls</code> set to <code>true</code>.</p>"""
    control_finding_generator: NotRequired[
        "capo_securityhub.types.control_finding_generator.ControlFindingGenerator"
    ]
    """<p>Specifies whether the calling account has consolidated control findings turned on. If the value for this field is set to <code>SECURITY_CONTROL</code>, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.</p> <p>If the value for this field is set to <code>STANDARD_CONTROL</code>, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.</p> <p>The value for this field in a member account matches the value in the administrator account. For accounts that aren't part of an organization, the default value of this field is <code>SECURITY_CONTROL</code> if you enabled Security Hub CSPM on or after February 23, 2023.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeHubResponse) -> dict:
    out: dict = {}
    if "hub_arn" in value:
        out["HubArn"] = value["hub_arn"]
    if "subscribed_at" in value:
        out["SubscribedAt"] = value["subscribed_at"]
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


def deserialize_json(data: dict) -> DescribeHubResponse:
    out: DescribeHubResponse = {}  # type: ignore[typeddict-item]
    if "HubArn" in data:
        out["hub_arn"] = data["HubArn"]
    if "SubscribedAt" in data:
        out["subscribed_at"] = data["SubscribedAt"]
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
