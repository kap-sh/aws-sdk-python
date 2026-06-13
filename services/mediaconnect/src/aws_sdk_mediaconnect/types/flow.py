"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Flow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_entitlement
    import aws_sdk_mediaconnect.types.__list_of_media_stream
    import aws_sdk_mediaconnect.types.__list_of_output
    import aws_sdk_mediaconnect.types.__list_of_source
    import aws_sdk_mediaconnect.types.__list_of_vpc_interface
    import aws_sdk_mediaconnect.types.encoding_config
    import aws_sdk_mediaconnect.types.failover_config
    import aws_sdk_mediaconnect.types.flow_size
    import aws_sdk_mediaconnect.types.maintenance
    import aws_sdk_mediaconnect.types.monitoring_config
    import aws_sdk_mediaconnect.types.ndi_config
    import aws_sdk_mediaconnect.types.source
    import aws_sdk_mediaconnect.types.status


class Flow(TypedDict):
    availability_zone: NotRequired["str"]
    """<p> The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current Amazon Web Services Region.</p>"""
    description: NotRequired["str"]
    """<p> A description of the flow. This value is not used or seen outside of the current MediaConnect account.</p>"""
    egress_ip: NotRequired["str"]
    """<p> The IP address from which video will be sent to output destinations.</p>"""
    entitlements: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_entitlement.__listOfEntitlement"
    ]
    """<p> The entitlements in this flow.</p>"""
    flow_arn: NotRequired["str"]
    """<p> The Amazon Resource Name (ARN) of the flow.</p>"""
    media_streams: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_media_stream.__listOfMediaStream"
    ]
    """<p> The media streams that are associated with the flow. After you associate a media stream with a source, you can also associate it with outputs on the flow.</p>"""
    name: NotRequired["str"]
    """<p> The name of the flow.</p>"""
    outputs: NotRequired["aws_sdk_mediaconnect.types.__list_of_output.__listOfOutput"]
    """<p> The outputs in this flow.</p>"""
    source: NotRequired["aws_sdk_mediaconnect.types.source.Source"]
    """<p> The source for the flow. </p>"""
    source_failover_config: NotRequired[
        "aws_sdk_mediaconnect.types.failover_config.FailoverConfig"
    ]
    """<p> The settings for the source failover. </p>"""
    sources: NotRequired["aws_sdk_mediaconnect.types.__list_of_source.__listOfSource"]
    """<p>The settings for the sources that are assigned to the flow. </p>"""
    status: NotRequired["aws_sdk_mediaconnect.types.status.Status"]
    """<p> The current status of the flow.</p>"""
    vpc_interfaces: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_vpc_interface.__listOfVpcInterface"
    ]
    """<p> The VPC Interfaces for this flow.</p>"""
    maintenance: NotRequired["aws_sdk_mediaconnect.types.maintenance.Maintenance"]
    """<p> The maintenance settings for the flow. </p>"""
    source_monitoring_config: NotRequired[
        "aws_sdk_mediaconnect.types.monitoring_config.MonitoringConfig"
    ]
    """<p> The settings for source monitoring. </p>"""
    flow_size: NotRequired["aws_sdk_mediaconnect.types.flow_size.FlowSize"]
    """<p> Determines the processing capacity and feature set of the flow. </p>"""
    ndi_config: NotRequired["aws_sdk_mediaconnect.types.ndi_config.NdiConfig"]
    """<p>Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output.</p>"""
    encoding_config: NotRequired[
        "aws_sdk_mediaconnect.types.encoding_config.EncodingConfig"
    ]
    """<p> The encoding configuration to apply to the NDI® source when transcoding it to a transport stream for downstream distribution. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Flow) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "description" in value:
        out["description"] = value["description"]
    if "egress_ip" in value:
        out["egressIp"] = value["egress_ip"]
    if "entitlements" in value:
        import aws_sdk_mediaconnect.types.__list_of_entitlement

        out["entitlements"] = (
            aws_sdk_mediaconnect.types.__list_of_entitlement.serialize_json(
                value["entitlements"]
            )
        )
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "media_streams" in value:
        import aws_sdk_mediaconnect.types.__list_of_media_stream

        out["mediaStreams"] = (
            aws_sdk_mediaconnect.types.__list_of_media_stream.serialize_json(
                value["media_streams"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "outputs" in value:
        import aws_sdk_mediaconnect.types.__list_of_output

        out["outputs"] = aws_sdk_mediaconnect.types.__list_of_output.serialize_json(
            value["outputs"]
        )
    if "source" in value:
        import aws_sdk_mediaconnect.types.source

        out["source"] = aws_sdk_mediaconnect.types.source.serialize_json(
            value["source"]
        )
    if "source_failover_config" in value:
        import aws_sdk_mediaconnect.types.failover_config

        out["sourceFailoverConfig"] = (
            aws_sdk_mediaconnect.types.failover_config.serialize_json(
                value["source_failover_config"]
            )
        )
    if "sources" in value:
        import aws_sdk_mediaconnect.types.__list_of_source

        out["sources"] = aws_sdk_mediaconnect.types.__list_of_source.serialize_json(
            value["sources"]
        )
    if "status" in value:
        import aws_sdk_mediaconnect.types.status

        out["status"] = aws_sdk_mediaconnect.types.status.serialize_json(
            value["status"]
        )
    if "vpc_interfaces" in value:
        import aws_sdk_mediaconnect.types.__list_of_vpc_interface

        out["vpcInterfaces"] = (
            aws_sdk_mediaconnect.types.__list_of_vpc_interface.serialize_json(
                value["vpc_interfaces"]
            )
        )
    if "maintenance" in value:
        import aws_sdk_mediaconnect.types.maintenance

        out["maintenance"] = aws_sdk_mediaconnect.types.maintenance.serialize_json(
            value["maintenance"]
        )
    if "source_monitoring_config" in value:
        import aws_sdk_mediaconnect.types.monitoring_config

        out["sourceMonitoringConfig"] = (
            aws_sdk_mediaconnect.types.monitoring_config.serialize_json(
                value["source_monitoring_config"]
            )
        )
    if "flow_size" in value:
        import aws_sdk_mediaconnect.types.flow_size

        out["flowSize"] = aws_sdk_mediaconnect.types.flow_size.serialize_json(
            value["flow_size"]
        )
    if "ndi_config" in value:
        import aws_sdk_mediaconnect.types.ndi_config

        out["ndiConfig"] = aws_sdk_mediaconnect.types.ndi_config.serialize_json(
            value["ndi_config"]
        )
    if "encoding_config" in value:
        import aws_sdk_mediaconnect.types.encoding_config

        out["encodingConfig"] = (
            aws_sdk_mediaconnect.types.encoding_config.serialize_json(
                value["encoding_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> Flow:
    out: Flow = {}  # type: ignore[typeddict-item]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "description" in data:
        out["description"] = data["description"]
    if "egressIp" in data:
        out["egress_ip"] = data["egressIp"]
    if "entitlements" in data:
        import aws_sdk_mediaconnect.types.__list_of_entitlement

        out["entitlements"] = (
            aws_sdk_mediaconnect.types.__list_of_entitlement.deserialize_json(
                data["entitlements"]
            )
        )
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "mediaStreams" in data:
        import aws_sdk_mediaconnect.types.__list_of_media_stream

        out["media_streams"] = (
            aws_sdk_mediaconnect.types.__list_of_media_stream.deserialize_json(
                data["mediaStreams"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "outputs" in data:
        import aws_sdk_mediaconnect.types.__list_of_output

        out["outputs"] = aws_sdk_mediaconnect.types.__list_of_output.deserialize_json(
            data["outputs"]
        )
    if "source" in data:
        import aws_sdk_mediaconnect.types.source

        out["source"] = aws_sdk_mediaconnect.types.source.deserialize_json(
            data["source"]
        )
    if "sourceFailoverConfig" in data:
        import aws_sdk_mediaconnect.types.failover_config

        out["source_failover_config"] = (
            aws_sdk_mediaconnect.types.failover_config.deserialize_json(
                data["sourceFailoverConfig"]
            )
        )
    if "sources" in data:
        import aws_sdk_mediaconnect.types.__list_of_source

        out["sources"] = aws_sdk_mediaconnect.types.__list_of_source.deserialize_json(
            data["sources"]
        )
    if "status" in data:
        import aws_sdk_mediaconnect.types.status

        out["status"] = aws_sdk_mediaconnect.types.status.deserialize_json(
            data["status"]
        )
    if "vpcInterfaces" in data:
        import aws_sdk_mediaconnect.types.__list_of_vpc_interface

        out["vpc_interfaces"] = (
            aws_sdk_mediaconnect.types.__list_of_vpc_interface.deserialize_json(
                data["vpcInterfaces"]
            )
        )
    if "maintenance" in data:
        import aws_sdk_mediaconnect.types.maintenance

        out["maintenance"] = aws_sdk_mediaconnect.types.maintenance.deserialize_json(
            data["maintenance"]
        )
    if "sourceMonitoringConfig" in data:
        import aws_sdk_mediaconnect.types.monitoring_config

        out["source_monitoring_config"] = (
            aws_sdk_mediaconnect.types.monitoring_config.deserialize_json(
                data["sourceMonitoringConfig"]
            )
        )
    if "flowSize" in data:
        import aws_sdk_mediaconnect.types.flow_size

        out["flow_size"] = aws_sdk_mediaconnect.types.flow_size.deserialize_json(
            data["flowSize"]
        )
    if "ndiConfig" in data:
        import aws_sdk_mediaconnect.types.ndi_config

        out["ndi_config"] = aws_sdk_mediaconnect.types.ndi_config.deserialize_json(
            data["ndiConfig"]
        )
    if "encodingConfig" in data:
        import aws_sdk_mediaconnect.types.encoding_config

        out["encoding_config"] = (
            aws_sdk_mediaconnect.types.encoding_config.deserialize_json(
                data["encodingConfig"]
            )
        )
    return out
