"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_media_stream_output_configuration_request
    import aws_sdk_mediaconnect.types.__list_of_string
    import aws_sdk_mediaconnect.types.__map_of_string
    import aws_sdk_mediaconnect.types.encryption
    import aws_sdk_mediaconnect.types.flow_transit_encryption
    import aws_sdk_mediaconnect.types.ndi_output_timecode_source
    import aws_sdk_mediaconnect.types.output_status
    import aws_sdk_mediaconnect.types.protocol
    import aws_sdk_mediaconnect.types.state
    import aws_sdk_mediaconnect.types.vpc_interface_attachment


class AddOutputRequest(TypedDict, closed=True):
    cidr_allow_list: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_string.__listOfString"
    ]
    """<p> The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>"""
    description: NotRequired["str"]
    """<p> A description of the output. This description appears only on the Audit Manager console and will not be seen by the end user.</p>"""
    destination: NotRequired["str"]
    """<p> The IP address from which video will be sent to output destinations.</p>"""
    encryption: NotRequired["aws_sdk_mediaconnect.types.encryption.Encryption"]
    """<p> The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.</p>"""
    max_latency: NotRequired["int"]
    """<p> The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.</p>"""
    media_stream_output_configurations: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_media_stream_output_configuration_request.__listOfMediaStreamOutputConfigurationRequest"
    ]
    """<p> The media streams that are associated with the output, and the parameters for those associations.</p>"""
    min_latency: NotRequired["int"]
    """<p> The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.</p>"""
    name: NotRequired["str"]
    """<p> The name of the output. This value must be unique within the current flow.</p>"""
    port: NotRequired["int"]
    """<p> The port to use when content is distributed to this output.</p>"""
    protocol: NotRequired["aws_sdk_mediaconnect.types.protocol.Protocol"]
    """<p> The protocol to use for the output.</p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>"""
    remote_id: NotRequired["str"]
    """<p> The remote ID for the Zixi-pull output stream.</p>"""
    sender_control_port: NotRequired["int"]
    """<p> The port that the flow uses to send outbound requests to initiate connection with the sender.</p>"""
    smoothing_latency: NotRequired["int"]
    """<p> The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.</p>"""
    stream_id: NotRequired["str"]
    """<p> The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.</p>"""
    vpc_interface_attachment: NotRequired[
        "aws_sdk_mediaconnect.types.vpc_interface_attachment.VpcInterfaceAttachment"
    ]
    """<p> The name of the VPC interface attachment to use for this output.</p>"""
    output_status: NotRequired["aws_sdk_mediaconnect.types.output_status.OutputStatus"]
    """<p> An indication of whether the new output should be enabled or disabled as soon as it is created. If you don't specify the outputStatus field in your request, MediaConnect sets it to ENABLED.</p>"""
    ndi_speed_hq_quality: NotRequired["int"]
    """<p>A quality setting for the NDI Speed HQ encoder. </p>"""
    ndi_program_name: NotRequired["str"]
    """<p> A suffix for the name of the NDI® sender that the flow creates. If a custom name isn't specified, MediaConnect uses the output name. </p>"""
    output_tags: NotRequired["aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"]
    """<p> The key-value pairs that can be used to tag and organize the output. </p>"""
    router_integration_state: NotRequired["aws_sdk_mediaconnect.types.state.State"]
    """<p>Indicates whether to enable or disable router integration when creating a new flow output.</p>"""
    router_integration_transit_encryption: NotRequired[
        "aws_sdk_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
    ]
    ndi_output_timecode_source: NotRequired[
        "aws_sdk_mediaconnect.types.ndi_output_timecode_source.NdiOutputTimecodeSource"
    ]
    """<p>Controls how MediaConnect generates timecodes for NDI output frames. If you don't specify this field, MediaConnect uses <code>EMBEDDED_TIMECODE</code>.</p> <ul> <li> <p> <code>EMBEDDED_TIMECODE</code> (default) - Preserves timecodes from the input transport stream. The timecodes must be embedded in the video stream as SEI timing messages. If no embedded timecode is detected, MediaConnect uses the UTC system time instead.</p> </li> <li> <p> <code>UTC_SYSTEM_TIME</code> - Generates timecodes based on the system clock time when each frame is sent.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddOutputRequest) -> dict:
    out: dict = {}
    if "cidr_allow_list" in value:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["cidrAllowList"] = (
            aws_sdk_mediaconnect.types.__list_of_string.serialize_json(
                value["cidr_allow_list"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "destination" in value:
        out["destination"] = value["destination"]
    if "encryption" in value:
        import aws_sdk_mediaconnect.types.encryption

        out["encryption"] = aws_sdk_mediaconnect.types.encryption.serialize_json(
            value["encryption"]
        )
    if "max_latency" in value:
        out["maxLatency"] = value["max_latency"]
    if "media_stream_output_configurations" in value:
        import aws_sdk_mediaconnect.types.__list_of_media_stream_output_configuration_request

        out["mediaStreamOutputConfigurations"] = (
            aws_sdk_mediaconnect.types.__list_of_media_stream_output_configuration_request.serialize_json(
                value["media_stream_output_configurations"]
            )
        )
    if "min_latency" in value:
        out["minLatency"] = value["min_latency"]
    if "name" in value:
        out["name"] = value["name"]
    if "port" in value:
        out["port"] = value["port"]
    if "protocol" in value:
        import aws_sdk_mediaconnect.types.protocol

        out["protocol"] = aws_sdk_mediaconnect.types.protocol.serialize_json(
            value["protocol"]
        )
    if "remote_id" in value:
        out["remoteId"] = value["remote_id"]
    if "sender_control_port" in value:
        out["senderControlPort"] = value["sender_control_port"]
    if "smoothing_latency" in value:
        out["smoothingLatency"] = value["smoothing_latency"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "vpc_interface_attachment" in value:
        import aws_sdk_mediaconnect.types.vpc_interface_attachment

        out["vpcInterfaceAttachment"] = (
            aws_sdk_mediaconnect.types.vpc_interface_attachment.serialize_json(
                value["vpc_interface_attachment"]
            )
        )
    if "output_status" in value:
        import aws_sdk_mediaconnect.types.output_status

        out["outputStatus"] = aws_sdk_mediaconnect.types.output_status.serialize_json(
            value["output_status"]
        )
    if "ndi_speed_hq_quality" in value:
        out["ndiSpeedHqQuality"] = value["ndi_speed_hq_quality"]
    if "ndi_program_name" in value:
        out["ndiProgramName"] = value["ndi_program_name"]
    if "output_tags" in value:
        import aws_sdk_mediaconnect.types.__map_of_string

        out["outputTags"] = aws_sdk_mediaconnect.types.__map_of_string.serialize_json(
            value["output_tags"]
        )
    if "router_integration_state" in value:
        import aws_sdk_mediaconnect.types.state

        out["routerIntegrationState"] = aws_sdk_mediaconnect.types.state.serialize_json(
            value["router_integration_state"]
        )
    if "router_integration_transit_encryption" in value:
        import aws_sdk_mediaconnect.types.flow_transit_encryption

        out["routerIntegrationTransitEncryption"] = (
            aws_sdk_mediaconnect.types.flow_transit_encryption.serialize_json(
                value["router_integration_transit_encryption"]
            )
        )
    if "ndi_output_timecode_source" in value:
        import aws_sdk_mediaconnect.types.ndi_output_timecode_source

        out["ndiOutputTimecodeSource"] = (
            aws_sdk_mediaconnect.types.ndi_output_timecode_source.serialize_json(
                value["ndi_output_timecode_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddOutputRequest:
    out: AddOutputRequest = {}  # type: ignore[typeddict-item]
    if "cidrAllowList" in data:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["cidr_allow_list"] = (
            aws_sdk_mediaconnect.types.__list_of_string.deserialize_json(
                data["cidrAllowList"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "destination" in data:
        out["destination"] = data["destination"]
    if "encryption" in data:
        import aws_sdk_mediaconnect.types.encryption

        out["encryption"] = aws_sdk_mediaconnect.types.encryption.deserialize_json(
            data["encryption"]
        )
    if "maxLatency" in data:
        out["max_latency"] = data["maxLatency"]
    if "mediaStreamOutputConfigurations" in data:
        import aws_sdk_mediaconnect.types.__list_of_media_stream_output_configuration_request

        out["media_stream_output_configurations"] = (
            aws_sdk_mediaconnect.types.__list_of_media_stream_output_configuration_request.deserialize_json(
                data["mediaStreamOutputConfigurations"]
            )
        )
    if "minLatency" in data:
        out["min_latency"] = data["minLatency"]
    if "name" in data:
        out["name"] = data["name"]
    if "port" in data:
        out["port"] = data["port"]
    if "protocol" in data:
        import aws_sdk_mediaconnect.types.protocol

        out["protocol"] = aws_sdk_mediaconnect.types.protocol.deserialize_json(
            data["protocol"]
        )
    if "remoteId" in data:
        out["remote_id"] = data["remoteId"]
    if "senderControlPort" in data:
        out["sender_control_port"] = data["senderControlPort"]
    if "smoothingLatency" in data:
        out["smoothing_latency"] = data["smoothingLatency"]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "vpcInterfaceAttachment" in data:
        import aws_sdk_mediaconnect.types.vpc_interface_attachment

        out["vpc_interface_attachment"] = (
            aws_sdk_mediaconnect.types.vpc_interface_attachment.deserialize_json(
                data["vpcInterfaceAttachment"]
            )
        )
    if "outputStatus" in data:
        import aws_sdk_mediaconnect.types.output_status

        out["output_status"] = (
            aws_sdk_mediaconnect.types.output_status.deserialize_json(
                data["outputStatus"]
            )
        )
    if "ndiSpeedHqQuality" in data:
        out["ndi_speed_hq_quality"] = data["ndiSpeedHqQuality"]
    if "ndiProgramName" in data:
        out["ndi_program_name"] = data["ndiProgramName"]
    if "outputTags" in data:
        import aws_sdk_mediaconnect.types.__map_of_string

        out["output_tags"] = (
            aws_sdk_mediaconnect.types.__map_of_string.deserialize_json(
                data["outputTags"]
            )
        )
    if "routerIntegrationState" in data:
        import aws_sdk_mediaconnect.types.state

        out["router_integration_state"] = (
            aws_sdk_mediaconnect.types.state.deserialize_json(
                data["routerIntegrationState"]
            )
        )
    if "routerIntegrationTransitEncryption" in data:
        import aws_sdk_mediaconnect.types.flow_transit_encryption

        out["router_integration_transit_encryption"] = (
            aws_sdk_mediaconnect.types.flow_transit_encryption.deserialize_json(
                data["routerIntegrationTransitEncryption"]
            )
        )
    if "ndiOutputTimecodeSource" in data:
        import aws_sdk_mediaconnect.types.ndi_output_timecode_source

        out["ndi_output_timecode_source"] = (
            aws_sdk_mediaconnect.types.ndi_output_timecode_source.deserialize_json(
                data["ndiOutputTimecodeSource"]
            )
        )
    return out
