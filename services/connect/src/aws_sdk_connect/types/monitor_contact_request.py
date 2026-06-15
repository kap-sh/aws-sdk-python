"""Generated from Smithy shape ``com.amazonaws.connect#MonitorContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_resource_id
    import aws_sdk_connect.types.allowed_monitor_capabilities
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.instance_id


class MonitorContactRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact.</p>"""
    user_id: "aws_sdk_connect.types.agent_resource_id.AgentResourceId"
    """<p>The identifier of the user account.</p>"""
    allowed_monitor_capabilities: NotRequired[
        "aws_sdk_connect.types.allowed_monitor_capabilities.AllowedMonitorCapabilities"
    ]
    """<p>Specify which monitoring actions the user is allowed to take. For example, whether the user is allowed to escalate from silent monitoring to barge. AllowedMonitorCapabilities is required if barge is enabled.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    out["UserId"] = value["user_id"]
    if "allowed_monitor_capabilities" in value:
        import aws_sdk_connect.types.allowed_monitor_capabilities

        out["AllowedMonitorCapabilities"] = (
            aws_sdk_connect.types.allowed_monitor_capabilities.serialize_json(
                value["allowed_monitor_capabilities"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> MonitorContactRequest:
    out: MonitorContactRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("MonitorContactRequest.instance_id required")
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("MonitorContactRequest.contact_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("MonitorContactRequest.user_id required")
    if "AllowedMonitorCapabilities" in data:
        import aws_sdk_connect.types.allowed_monitor_capabilities

        out["allowed_monitor_capabilities"] = (
            aws_sdk_connect.types.allowed_monitor_capabilities.deserialize_json(
                data["AllowedMonitorCapabilities"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
