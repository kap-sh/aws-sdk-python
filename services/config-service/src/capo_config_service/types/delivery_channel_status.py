"""Generated from Smithy shape ``com.amazonaws.configservice#DeliveryChannelStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_export_delivery_info
    import capo_config_service.types.config_stream_delivery_info
    import capo_config_service.types.string


class DeliveryChannelStatus(TypedDict, closed=True):
    name: NotRequired["capo_config_service.types.string.String"]
    """<p>The name of the delivery channel.</p>"""
    config_snapshot_delivery_info: NotRequired[
        "capo_config_service.types.config_export_delivery_info.ConfigExportDeliveryInfo"
    ]
    """<p>A list containing the status of the delivery of the snapshot to the specified Amazon S3 bucket.</p>"""
    config_history_delivery_info: NotRequired[
        "capo_config_service.types.config_export_delivery_info.ConfigExportDeliveryInfo"
    ]
    """<p>A list that contains the status of the delivery of the configuration history to the specified Amazon S3 bucket.</p>"""
    config_stream_delivery_info: NotRequired[
        "capo_config_service.types.config_stream_delivery_info.ConfigStreamDeliveryInfo"
    ]
    """<p>A list containing the status of the delivery of the configuration stream notification to the specified Amazon SNS topic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryChannelStatus) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "config_snapshot_delivery_info" in value:
        import capo_config_service.types.config_export_delivery_info

        out["configSnapshotDeliveryInfo"] = (
            capo_config_service.types.config_export_delivery_info.serialize_aws_json_1_1(
                value["config_snapshot_delivery_info"]
            )
        )
    if "config_history_delivery_info" in value:
        import capo_config_service.types.config_export_delivery_info

        out["configHistoryDeliveryInfo"] = (
            capo_config_service.types.config_export_delivery_info.serialize_aws_json_1_1(
                value["config_history_delivery_info"]
            )
        )
    if "config_stream_delivery_info" in value:
        import capo_config_service.types.config_stream_delivery_info

        out["configStreamDeliveryInfo"] = (
            capo_config_service.types.config_stream_delivery_info.serialize_aws_json_1_1(
                value["config_stream_delivery_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliveryChannelStatus:
    out: DeliveryChannelStatus = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "configSnapshotDeliveryInfo" in data:
        import capo_config_service.types.config_export_delivery_info

        out["config_snapshot_delivery_info"] = (
            capo_config_service.types.config_export_delivery_info.deserialize_aws_json_1_1(
                data["configSnapshotDeliveryInfo"]
            )
        )
    if "configHistoryDeliveryInfo" in data:
        import capo_config_service.types.config_export_delivery_info

        out["config_history_delivery_info"] = (
            capo_config_service.types.config_export_delivery_info.deserialize_aws_json_1_1(
                data["configHistoryDeliveryInfo"]
            )
        )
    if "configStreamDeliveryInfo" in data:
        import capo_config_service.types.config_stream_delivery_info

        out["config_stream_delivery_info"] = (
            capo_config_service.types.config_stream_delivery_info.deserialize_aws_json_1_1(
                data["configStreamDeliveryInfo"]
            )
        )
    return out
