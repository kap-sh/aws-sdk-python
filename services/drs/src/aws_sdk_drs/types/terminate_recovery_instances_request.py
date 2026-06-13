"""Generated from Smithy shape ``com.amazonaws.drs#TerminateRecoveryInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.recovery_instances_for_termination_request


class TerminateRecoveryInstancesRequest(TypedDict):
    recovery_instance_i_ds: "aws_sdk_drs.types.recovery_instances_for_termination_request.RecoveryInstancesForTerminationRequest"
    """<p>The IDs of the Recovery Instances that should be terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateRecoveryInstancesRequest) -> dict:
    out: dict = {}
    import aws_sdk_drs.types.recovery_instances_for_termination_request

    out["recoveryInstanceIDs"] = (
        aws_sdk_drs.types.recovery_instances_for_termination_request.serialize_json(
            value["recovery_instance_i_ds"]
        )
    )
    return out


def deserialize_json(data: dict) -> TerminateRecoveryInstancesRequest:
    out: TerminateRecoveryInstancesRequest = {}  # type: ignore[typeddict-item]
    if "recoveryInstanceIDs" in data:
        import aws_sdk_drs.types.recovery_instances_for_termination_request

        out["recovery_instance_i_ds"] = (
            aws_sdk_drs.types.recovery_instances_for_termination_request.deserialize_json(
                data["recoveryInstanceIDs"]
            )
        )
    else:
        raise DeserializationError(
            "TerminateRecoveryInstancesRequest.recovery_instance_i_ds required"
        )
    return out
