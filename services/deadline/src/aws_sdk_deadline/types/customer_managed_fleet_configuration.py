"""Generated from Smithy shape ``com.amazonaws.deadline#CustomerManagedFleetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.auto_scaling_mode
    import aws_sdk_deadline.types.customer_managed_auto_scaling_configuration
    import aws_sdk_deadline.types.customer_managed_worker_capabilities
    import aws_sdk_deadline.types.storage_profile_id
    import aws_sdk_deadline.types.tag_propagation_mode


class CustomerManagedFleetConfiguration(TypedDict, closed=True):
    mode: "aws_sdk_deadline.types.auto_scaling_mode.AutoScalingMode"
    """<p>The Auto Scaling mode for the customer managed fleet.</p>"""
    auto_scaling_configuration: NotRequired[
        "aws_sdk_deadline.types.customer_managed_auto_scaling_configuration.CustomerManagedAutoScalingConfiguration"
    ]
    """<p>The auto scaling configuration settings for the customer managed fleet.</p>"""
    worker_capabilities: "aws_sdk_deadline.types.customer_managed_worker_capabilities.CustomerManagedWorkerCapabilities"
    """<p>The worker capabilities for the customer managed fleet.</p>"""
    storage_profile_id: NotRequired[
        "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    ]
    """<p>The storage profile ID for the customer managed fleet.</p>"""
    tag_propagation_mode: NotRequired[
        "aws_sdk_deadline.types.tag_propagation_mode.TagPropagationMode"
    ]
    """<p>The tag propagation mode for the customer managed fleet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerManagedFleetConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.auto_scaling_mode

    out["mode"] = aws_sdk_deadline.types.auto_scaling_mode.serialize_json(value["mode"])
    if "auto_scaling_configuration" in value:
        import aws_sdk_deadline.types.customer_managed_auto_scaling_configuration

        out["autoScalingConfiguration"] = (
            aws_sdk_deadline.types.customer_managed_auto_scaling_configuration.serialize_json(
                value["auto_scaling_configuration"]
            )
        )
    import aws_sdk_deadline.types.customer_managed_worker_capabilities

    out["workerCapabilities"] = (
        aws_sdk_deadline.types.customer_managed_worker_capabilities.serialize_json(
            value["worker_capabilities"]
        )
    )
    if "storage_profile_id" in value:
        out["storageProfileId"] = value["storage_profile_id"]
    if "tag_propagation_mode" in value:
        import aws_sdk_deadline.types.tag_propagation_mode

        out["tagPropagationMode"] = (
            aws_sdk_deadline.types.tag_propagation_mode.serialize_json(
                value["tag_propagation_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomerManagedFleetConfiguration:
    out: CustomerManagedFleetConfiguration = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_deadline.types.auto_scaling_mode

        out["mode"] = aws_sdk_deadline.types.auto_scaling_mode.deserialize_json(
            data["mode"]
        )
    else:
        raise DeserializationError("CustomerManagedFleetConfiguration.mode required")
    if "autoScalingConfiguration" in data:
        import aws_sdk_deadline.types.customer_managed_auto_scaling_configuration

        out["auto_scaling_configuration"] = (
            aws_sdk_deadline.types.customer_managed_auto_scaling_configuration.deserialize_json(
                data["autoScalingConfiguration"]
            )
        )
    if "workerCapabilities" in data:
        import aws_sdk_deadline.types.customer_managed_worker_capabilities

        out["worker_capabilities"] = (
            aws_sdk_deadline.types.customer_managed_worker_capabilities.deserialize_json(
                data["workerCapabilities"]
            )
        )
    else:
        raise DeserializationError(
            "CustomerManagedFleetConfiguration.worker_capabilities required"
        )
    if "storageProfileId" in data:
        out["storage_profile_id"] = data["storageProfileId"]
    if "tagPropagationMode" in data:
        import aws_sdk_deadline.types.tag_propagation_mode

        out["tag_propagation_mode"] = (
            aws_sdk_deadline.types.tag_propagation_mode.deserialize_json(
                data["tagPropagationMode"]
            )
        )
    return out
