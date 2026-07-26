"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.enabled
    import capo_pinpoint_email.types.general_enforcement_status
    import capo_pinpoint_email.types.send_quota


class GetAccountResponse(TypedDict, closed=True):
    send_quota: NotRequired["capo_pinpoint_email.types.send_quota.SendQuota"]
    """<p>An object that contains information about the per-day and per-second sending limits for your Amazon Pinpoint account in the current AWS Region.</p>"""
    sending_enabled: "capo_pinpoint_email.types.enabled.Enabled"
    """<p>Indicates whether or not email sending is enabled for your Amazon Pinpoint account in the current AWS Region.</p>"""
    dedicated_ip_auto_warmup_enabled: "capo_pinpoint_email.types.enabled.Enabled"
    """<p>Indicates whether or not the automatic warm-up feature is enabled for dedicated IP addresses that are associated with your account.</p>"""
    enforcement_status: NotRequired[
        "capo_pinpoint_email.types.general_enforcement_status.GeneralEnforcementStatus"
    ]
    """<p>The reputation status of your Amazon Pinpoint account. The status can be one of the following:</p> <ul> <li> <p> <code>HEALTHY</code> – There are no reputation-related issues that currently impact your account.</p> </li> <li> <p> <code>PROBATION</code> – We've identified some issues with your Amazon Pinpoint account. We're placing your account under review while you work on correcting these issues.</p> </li> <li> <p> <code>SHUTDOWN</code> – Your account's ability to send email is currently paused because of an issue with the email sent from your account. When you correct the issue, you can contact us and request that your account's ability to send email is resumed.</p> </li> </ul>"""
    production_access_enabled: "capo_pinpoint_email.types.enabled.Enabled"
    """<p>Indicates whether or not your account has production access in the current AWS Region.</p> <p>If the value is <code>false</code>, then your account is in the <i>sandbox</i>. When your account is in the sandbox, you can only send email to verified identities. Additionally, the maximum number of emails you can send in a 24-hour period (your sending quota) is 200, and the maximum number of emails you can send per second (your maximum sending rate) is 1.</p> <p>If the value is <code>true</code>, then your account has production access. When your account has production access, you can send email to any address. The sending quota and maximum sending rate for your account vary based on your specific use case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountResponse) -> dict:
    out: dict = {}
    if "send_quota" in value:
        import capo_pinpoint_email.types.send_quota

        out["SendQuota"] = capo_pinpoint_email.types.send_quota.serialize_json(
            value["send_quota"]
        )
    out["SendingEnabled"] = value.get("sending_enabled", False)
    out["DedicatedIpAutoWarmupEnabled"] = value.get(
        "dedicated_ip_auto_warmup_enabled", False
    )
    if "enforcement_status" in value:
        out["EnforcementStatus"] = value["enforcement_status"]
    out["ProductionAccessEnabled"] = value.get("production_access_enabled", False)
    return out


def deserialize_json(data: dict) -> GetAccountResponse:
    out: GetAccountResponse = {}  # type: ignore[typeddict-item]
    if "SendQuota" in data:
        import capo_pinpoint_email.types.send_quota

        out["send_quota"] = capo_pinpoint_email.types.send_quota.deserialize_json(
            data["SendQuota"]
        )
    if "SendingEnabled" in data:
        out["sending_enabled"] = data["SendingEnabled"]
    else:
        out["sending_enabled"] = False
    if "DedicatedIpAutoWarmupEnabled" in data:
        out["dedicated_ip_auto_warmup_enabled"] = data["DedicatedIpAutoWarmupEnabled"]
    else:
        out["dedicated_ip_auto_warmup_enabled"] = False
    if "EnforcementStatus" in data:
        out["enforcement_status"] = data["EnforcementStatus"]
    if "ProductionAccessEnabled" in data:
        out["production_access_enabled"] = data["ProductionAccessEnabled"]
    else:
        out["production_access_enabled"] = False
    return out
