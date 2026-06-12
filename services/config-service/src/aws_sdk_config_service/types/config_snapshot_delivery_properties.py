"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigSnapshotDeliveryProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.maximum_execution_frequency


class ConfigSnapshotDeliveryProperties(TypedDict):
    delivery_frequency: NotRequired[
        "aws_sdk_config_service.types.maximum_execution_frequency.MaximumExecutionFrequency"
    ]
    """<p>The frequency with which Config delivers configuration snapshots.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigSnapshotDeliveryProperties) -> dict:
    out: dict = {}
    if "delivery_frequency" in value:
        import aws_sdk_config_service.types.maximum_execution_frequency

        out["deliveryFrequency"] = (
            aws_sdk_config_service.types.maximum_execution_frequency.serialize_aws_json_1_1(
                value["delivery_frequency"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigSnapshotDeliveryProperties:
    out: ConfigSnapshotDeliveryProperties = {}  # type: ignore[typeddict-item]
    if "deliveryFrequency" in data:
        import aws_sdk_config_service.types.maximum_execution_frequency

        out["delivery_frequency"] = (
            aws_sdk_config_service.types.maximum_execution_frequency.deserialize_aws_json_1_1(
                data["deliveryFrequency"]
            )
        )
    return out
