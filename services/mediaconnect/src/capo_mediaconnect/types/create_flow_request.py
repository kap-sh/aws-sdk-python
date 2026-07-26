"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_add_media_stream_request
    import capo_mediaconnect.types.__list_of_add_output_request
    import capo_mediaconnect.types.__list_of_grant_entitlement_request
    import capo_mediaconnect.types.__list_of_set_source_request
    import capo_mediaconnect.types.__list_of_vpc_interface_request
    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.add_maintenance
    import capo_mediaconnect.types.encoding_config
    import capo_mediaconnect.types.failover_config
    import capo_mediaconnect.types.flow_size
    import capo_mediaconnect.types.monitoring_config
    import capo_mediaconnect.types.ndi_config
    import capo_mediaconnect.types.set_source_request


class CreateFlowRequest(TypedDict, closed=True):
    availability_zone: NotRequired["str"]
    """<p> The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current Amazon Web Services Region.</p>"""
    entitlements: NotRequired[
        "capo_mediaconnect.types.__list_of_grant_entitlement_request.__listOfGrantEntitlementRequest"
    ]
    """<p> The entitlements that you want to grant on a flow.</p>"""
    media_streams: NotRequired[
        "capo_mediaconnect.types.__list_of_add_media_stream_request.__listOfAddMediaStreamRequest"
    ]
    """<p> The media streams that you want to add to the flow. You can associate these media streams with sources and outputs on the flow.</p>"""
    name: NotRequired["str"]
    """<p> The name of the flow.</p>"""
    outputs: NotRequired[
        "capo_mediaconnect.types.__list_of_add_output_request.__listOfAddOutputRequest"
    ]
    """<p> The outputs that you want to add to this flow.</p>"""
    source: NotRequired["capo_mediaconnect.types.set_source_request.SetSourceRequest"]
    """<p> The settings for the source that you want to use for the new flow. </p>"""
    source_failover_config: NotRequired[
        "capo_mediaconnect.types.failover_config.FailoverConfig"
    ]
    """<p> The settings for source failover. </p>"""
    sources: NotRequired[
        "capo_mediaconnect.types.__list_of_set_source_request.__listOfSetSourceRequest"
    ]
    """<p>The sources that are assigned to the flow. </p>"""
    vpc_interfaces: NotRequired[
        "capo_mediaconnect.types.__list_of_vpc_interface_request.__listOfVpcInterfaceRequest"
    ]
    """<p> The VPC interfaces you want on the flow.</p>"""
    maintenance: NotRequired["capo_mediaconnect.types.add_maintenance.AddMaintenance"]
    """<p> The maintenance settings you want to use for the flow. </p>"""
    source_monitoring_config: NotRequired[
        "capo_mediaconnect.types.monitoring_config.MonitoringConfig"
    ]
    """<p> The settings for source monitoring. </p>"""
    flow_size: NotRequired["capo_mediaconnect.types.flow_size.FlowSize"]
    """<p> Determines the processing capacity and feature set of the flow. Set this optional parameter to <code>LARGE</code> if you want to enable NDI sources or outputs on the flow. </p>"""
    ndi_config: NotRequired["capo_mediaconnect.types.ndi_config.NdiConfig"]
    """<p> Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output. </p>"""
    encoding_config: NotRequired[
        "capo_mediaconnect.types.encoding_config.EncodingConfig"
    ]
    flow_tags: NotRequired["capo_mediaconnect.types.__map_of_string.__mapOfString"]
    """<p> The key-value pairs that can be used to tag and organize the flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlowRequest) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "entitlements" in value:
        import capo_mediaconnect.types.__list_of_grant_entitlement_request

        out["entitlements"] = (
            capo_mediaconnect.types.__list_of_grant_entitlement_request.serialize_json(
                value["entitlements"]
            )
        )
    if "media_streams" in value:
        import capo_mediaconnect.types.__list_of_add_media_stream_request

        out["mediaStreams"] = (
            capo_mediaconnect.types.__list_of_add_media_stream_request.serialize_json(
                value["media_streams"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "outputs" in value:
        import capo_mediaconnect.types.__list_of_add_output_request

        out["outputs"] = (
            capo_mediaconnect.types.__list_of_add_output_request.serialize_json(
                value["outputs"]
            )
        )
    if "source" in value:
        import capo_mediaconnect.types.set_source_request

        out["source"] = capo_mediaconnect.types.set_source_request.serialize_json(
            value["source"]
        )
    if "source_failover_config" in value:
        import capo_mediaconnect.types.failover_config

        out["sourceFailoverConfig"] = (
            capo_mediaconnect.types.failover_config.serialize_json(
                value["source_failover_config"]
            )
        )
    if "sources" in value:
        import capo_mediaconnect.types.__list_of_set_source_request

        out["sources"] = (
            capo_mediaconnect.types.__list_of_set_source_request.serialize_json(
                value["sources"]
            )
        )
    if "vpc_interfaces" in value:
        import capo_mediaconnect.types.__list_of_vpc_interface_request

        out["vpcInterfaces"] = (
            capo_mediaconnect.types.__list_of_vpc_interface_request.serialize_json(
                value["vpc_interfaces"]
            )
        )
    if "maintenance" in value:
        import capo_mediaconnect.types.add_maintenance

        out["maintenance"] = capo_mediaconnect.types.add_maintenance.serialize_json(
            value["maintenance"]
        )
    if "source_monitoring_config" in value:
        import capo_mediaconnect.types.monitoring_config

        out["sourceMonitoringConfig"] = (
            capo_mediaconnect.types.monitoring_config.serialize_json(
                value["source_monitoring_config"]
            )
        )
    if "flow_size" in value:
        import capo_mediaconnect.types.flow_size

        out["flowSize"] = capo_mediaconnect.types.flow_size.serialize_json(
            value["flow_size"]
        )
    if "ndi_config" in value:
        import capo_mediaconnect.types.ndi_config

        out["ndiConfig"] = capo_mediaconnect.types.ndi_config.serialize_json(
            value["ndi_config"]
        )
    if "encoding_config" in value:
        import capo_mediaconnect.types.encoding_config

        out["encodingConfig"] = capo_mediaconnect.types.encoding_config.serialize_json(
            value["encoding_config"]
        )
    if "flow_tags" in value:
        import capo_mediaconnect.types.__map_of_string

        out["flowTags"] = capo_mediaconnect.types.__map_of_string.serialize_json(
            value["flow_tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateFlowRequest:
    out: CreateFlowRequest = {}  # type: ignore[typeddict-item]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "entitlements" in data:
        import capo_mediaconnect.types.__list_of_grant_entitlement_request

        out["entitlements"] = (
            capo_mediaconnect.types.__list_of_grant_entitlement_request.deserialize_json(
                data["entitlements"]
            )
        )
    if "mediaStreams" in data:
        import capo_mediaconnect.types.__list_of_add_media_stream_request

        out["media_streams"] = (
            capo_mediaconnect.types.__list_of_add_media_stream_request.deserialize_json(
                data["mediaStreams"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "outputs" in data:
        import capo_mediaconnect.types.__list_of_add_output_request

        out["outputs"] = (
            capo_mediaconnect.types.__list_of_add_output_request.deserialize_json(
                data["outputs"]
            )
        )
    if "source" in data:
        import capo_mediaconnect.types.set_source_request

        out["source"] = capo_mediaconnect.types.set_source_request.deserialize_json(
            data["source"]
        )
    if "sourceFailoverConfig" in data:
        import capo_mediaconnect.types.failover_config

        out["source_failover_config"] = (
            capo_mediaconnect.types.failover_config.deserialize_json(
                data["sourceFailoverConfig"]
            )
        )
    if "sources" in data:
        import capo_mediaconnect.types.__list_of_set_source_request

        out["sources"] = (
            capo_mediaconnect.types.__list_of_set_source_request.deserialize_json(
                data["sources"]
            )
        )
    if "vpcInterfaces" in data:
        import capo_mediaconnect.types.__list_of_vpc_interface_request

        out["vpc_interfaces"] = (
            capo_mediaconnect.types.__list_of_vpc_interface_request.deserialize_json(
                data["vpcInterfaces"]
            )
        )
    if "maintenance" in data:
        import capo_mediaconnect.types.add_maintenance

        out["maintenance"] = capo_mediaconnect.types.add_maintenance.deserialize_json(
            data["maintenance"]
        )
    if "sourceMonitoringConfig" in data:
        import capo_mediaconnect.types.monitoring_config

        out["source_monitoring_config"] = (
            capo_mediaconnect.types.monitoring_config.deserialize_json(
                data["sourceMonitoringConfig"]
            )
        )
    if "flowSize" in data:
        import capo_mediaconnect.types.flow_size

        out["flow_size"] = capo_mediaconnect.types.flow_size.deserialize_json(
            data["flowSize"]
        )
    if "ndiConfig" in data:
        import capo_mediaconnect.types.ndi_config

        out["ndi_config"] = capo_mediaconnect.types.ndi_config.deserialize_json(
            data["ndiConfig"]
        )
    if "encodingConfig" in data:
        import capo_mediaconnect.types.encoding_config

        out["encoding_config"] = (
            capo_mediaconnect.types.encoding_config.deserialize_json(
                data["encodingConfig"]
            )
        )
    if "flowTags" in data:
        import capo_mediaconnect.types.__map_of_string

        out["flow_tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["flowTags"]
        )
    return out
