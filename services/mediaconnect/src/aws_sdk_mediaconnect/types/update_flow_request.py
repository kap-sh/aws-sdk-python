"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.encoding_config
    import aws_sdk_mediaconnect.types.flow_arn
    import aws_sdk_mediaconnect.types.flow_size
    import aws_sdk_mediaconnect.types.monitoring_config
    import aws_sdk_mediaconnect.types.ndi_config
    import aws_sdk_mediaconnect.types.update_failover_config
    import aws_sdk_mediaconnect.types.update_maintenance


class UpdateFlowRequest(TypedDict):
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>"""
    source_failover_config: NotRequired[
        "aws_sdk_mediaconnect.types.update_failover_config.UpdateFailoverConfig"
    ]
    """<p> The settings for source failover. </p>"""
    maintenance: NotRequired[
        "aws_sdk_mediaconnect.types.update_maintenance.UpdateMaintenance"
    ]
    """<p> The maintenance setting of the flow. </p>"""
    source_monitoring_config: NotRequired[
        "aws_sdk_mediaconnect.types.monitoring_config.MonitoringConfig"
    ]
    """<p> The settings for source monitoring. </p>"""
    ndi_config: NotRequired["aws_sdk_mediaconnect.types.ndi_config.NdiConfig"]
    """<p> Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output. </p>"""
    flow_size: NotRequired["aws_sdk_mediaconnect.types.flow_size.FlowSize"]
    """<p> Determines the processing capacity and feature set of the flow. </p>"""
    encoding_config: NotRequired[
        "aws_sdk_mediaconnect.types.encoding_config.EncodingConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowRequest) -> dict:
    out: dict = {}
    if "source_failover_config" in value:
        import aws_sdk_mediaconnect.types.update_failover_config

        out["sourceFailoverConfig"] = (
            aws_sdk_mediaconnect.types.update_failover_config.serialize_json(
                value["source_failover_config"]
            )
        )
    if "maintenance" in value:
        import aws_sdk_mediaconnect.types.update_maintenance

        out["maintenance"] = (
            aws_sdk_mediaconnect.types.update_maintenance.serialize_json(
                value["maintenance"]
            )
        )
    if "source_monitoring_config" in value:
        import aws_sdk_mediaconnect.types.monitoring_config

        out["sourceMonitoringConfig"] = (
            aws_sdk_mediaconnect.types.monitoring_config.serialize_json(
                value["source_monitoring_config"]
            )
        )
    if "ndi_config" in value:
        import aws_sdk_mediaconnect.types.ndi_config

        out["ndiConfig"] = aws_sdk_mediaconnect.types.ndi_config.serialize_json(
            value["ndi_config"]
        )
    if "flow_size" in value:
        import aws_sdk_mediaconnect.types.flow_size

        out["flowSize"] = aws_sdk_mediaconnect.types.flow_size.serialize_json(
            value["flow_size"]
        )
    if "encoding_config" in value:
        import aws_sdk_mediaconnect.types.encoding_config

        out["encodingConfig"] = (
            aws_sdk_mediaconnect.types.encoding_config.serialize_json(
                value["encoding_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateFlowRequest:
    out: UpdateFlowRequest = {}  # type: ignore[typeddict-item]
    if "sourceFailoverConfig" in data:
        import aws_sdk_mediaconnect.types.update_failover_config

        out["source_failover_config"] = (
            aws_sdk_mediaconnect.types.update_failover_config.deserialize_json(
                data["sourceFailoverConfig"]
            )
        )
    if "maintenance" in data:
        import aws_sdk_mediaconnect.types.update_maintenance

        out["maintenance"] = (
            aws_sdk_mediaconnect.types.update_maintenance.deserialize_json(
                data["maintenance"]
            )
        )
    if "sourceMonitoringConfig" in data:
        import aws_sdk_mediaconnect.types.monitoring_config

        out["source_monitoring_config"] = (
            aws_sdk_mediaconnect.types.monitoring_config.deserialize_json(
                data["sourceMonitoringConfig"]
            )
        )
    if "ndiConfig" in data:
        import aws_sdk_mediaconnect.types.ndi_config

        out["ndi_config"] = aws_sdk_mediaconnect.types.ndi_config.deserialize_json(
            data["ndiConfig"]
        )
    if "flowSize" in data:
        import aws_sdk_mediaconnect.types.flow_size

        out["flow_size"] = aws_sdk_mediaconnect.types.flow_size.deserialize_json(
            data["flowSize"]
        )
    if "encodingConfig" in data:
        import aws_sdk_mediaconnect.types.encoding_config

        out["encoding_config"] = (
            aws_sdk_mediaconnect.types.encoding_config.deserialize_json(
                data["encodingConfig"]
            )
        )
    return out
