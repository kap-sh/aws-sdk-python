"""Generated from Smithy shape ``com.amazonaws.appflow#PrivateConnectionProvisioningState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.private_connection_provisioning_failure_cause
    import aws_sdk_appflow.types.private_connection_provisioning_failure_message
    import aws_sdk_appflow.types.private_connection_provisioning_status


class PrivateConnectionProvisioningState(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_appflow.types.private_connection_provisioning_status.PrivateConnectionProvisioningStatus"
    ]
    """<p> Specifies the private connection provisioning status. </p>"""
    failure_message: NotRequired[
        "aws_sdk_appflow.types.private_connection_provisioning_failure_message.PrivateConnectionProvisioningFailureMessage"
    ]
    """<p> Specifies the private connection provisioning failure reason. </p>"""
    failure_cause: NotRequired[
        "aws_sdk_appflow.types.private_connection_provisioning_failure_cause.PrivateConnectionProvisioningFailureCause"
    ]
    """<p> Specifies the private connection provisioning failure cause. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionProvisioningState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_appflow.types.private_connection_provisioning_status

        out["status"] = (
            aws_sdk_appflow.types.private_connection_provisioning_status.serialize_json(
                value["status"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "failure_cause" in value:
        import aws_sdk_appflow.types.private_connection_provisioning_failure_cause

        out["failureCause"] = (
            aws_sdk_appflow.types.private_connection_provisioning_failure_cause.serialize_json(
                value["failure_cause"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrivateConnectionProvisioningState:
    out: PrivateConnectionProvisioningState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_appflow.types.private_connection_provisioning_status

        out["status"] = (
            aws_sdk_appflow.types.private_connection_provisioning_status.deserialize_json(
                data["status"]
            )
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "failureCause" in data:
        import aws_sdk_appflow.types.private_connection_provisioning_failure_cause

        out["failure_cause"] = (
            aws_sdk_appflow.types.private_connection_provisioning_failure_cause.deserialize_json(
                data["failureCause"]
            )
        )
    return out
