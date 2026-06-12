"""Generated from Smithy shape ``com.amazonaws.batch#UpdateServiceEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.capacity_limits
    import aws_sdk_batch.types.service_environment_state
    import aws_sdk_batch.types.string


class UpdateServiceEnvironmentRequest(TypedDict):
    service_environment: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name or ARN of the service environment to update.</p>"""
    state: NotRequired[
        "aws_sdk_batch.types.service_environment_state.ServiceEnvironmentState"
    ]
    """<p>The state of the service environment. </p>"""
    capacity_limits: NotRequired["aws_sdk_batch.types.capacity_limits.CapacityLimits"]
    """<p>The capacity limits for the service environment. This defines the maximum resources that can be used by service jobs in this environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceEnvironmentRequest) -> dict:
    out: dict = {}
    if "service_environment" in value:
        out["serviceEnvironment"] = value["service_environment"]
    if "state" in value:
        import aws_sdk_batch.types.service_environment_state

        out["state"] = aws_sdk_batch.types.service_environment_state.serialize_json(
            value["state"]
        )
    if "capacity_limits" in value:
        import aws_sdk_batch.types.capacity_limits

        out["capacityLimits"] = aws_sdk_batch.types.capacity_limits.serialize_json(
            value["capacity_limits"]
        )
    return out


def deserialize_json(data: dict) -> UpdateServiceEnvironmentRequest:
    out: UpdateServiceEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "serviceEnvironment" in data:
        out["service_environment"] = data["serviceEnvironment"]
    if "state" in data:
        import aws_sdk_batch.types.service_environment_state

        out["state"] = aws_sdk_batch.types.service_environment_state.deserialize_json(
            data["state"]
        )
    if "capacityLimits" in data:
        import aws_sdk_batch.types.capacity_limits

        out["capacity_limits"] = aws_sdk_batch.types.capacity_limits.deserialize_json(
            data["capacityLimits"]
        )
    return out
