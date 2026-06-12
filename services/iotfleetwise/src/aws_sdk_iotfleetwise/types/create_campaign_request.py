"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateCampaignRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.campaign_name
    import aws_sdk_iotfleetwise.types.collection_scheme
    import aws_sdk_iotfleetwise.types.compression
    import aws_sdk_iotfleetwise.types.data_destination_configs
    import aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list
    import aws_sdk_iotfleetwise.types.data_partitions
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.diagnostics_mode
    import aws_sdk_iotfleetwise.types.priority
    import aws_sdk_iotfleetwise.types.signal_fetch_information_list
    import aws_sdk_iotfleetwise.types.signal_information_list
    import aws_sdk_iotfleetwise.types.spooling_mode
    import aws_sdk_iotfleetwise.types.tag_list
    import aws_sdk_iotfleetwise.types.timestamp
    import aws_sdk_iotfleetwise.types.uint32


class CreateCampaignRequest(TypedDict):
    name: "aws_sdk_iotfleetwise.types.campaign_name.campaignName"
    """<p> The name of the campaign to create. </p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p>An optional description of the campaign to help identify its purpose.</p>"""
    signal_catalog_arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p>The Amazon Resource Name (ARN) of the signal catalog to associate with the campaign. </p>"""
    target_arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p> The ARN of the vehicle or fleet to deploy a campaign to. </p>"""
    start_time: NotRequired["aws_sdk_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time, in milliseconds, to deliver a campaign after it was approved. If it's not specified, <code>0</code> is used.</p> <p>Default: <code>0</code> </p>"""
    expiry_time: NotRequired["aws_sdk_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time). Vehicle data isn't collected after the campaign expires. </p> <p>Default: 253402214400 (December 31, 9999, 00:00:00 UTC)</p>"""
    post_trigger_collection_duration: NotRequired[
        "aws_sdk_iotfleetwise.types.uint32.uint32"
    ]
    """<p>How long (in milliseconds) to collect raw data after a triggering event initiates the collection. If it's not specified, <code>0</code> is used.</p> <p>Default: <code>0</code> </p>"""
    diagnostics_mode: NotRequired[
        "aws_sdk_iotfleetwise.types.diagnostics_mode.DiagnosticsMode"
    ]
    """<p>Option for a vehicle to send diagnostic trouble codes to Amazon Web Services IoT FleetWise. If you want to send diagnostic trouble codes, use <code>SEND_ACTIVE_DTCS</code>. If it's not specified, <code>OFF</code> is used.</p> <p>Default: <code>OFF</code> </p>"""
    spooling_mode: NotRequired["aws_sdk_iotfleetwise.types.spooling_mode.SpoolingMode"]
    """<p>Determines whether to store collected data after a vehicle lost a connection with the cloud. After a connection is re-established, the data is automatically forwarded to Amazon Web Services IoT FleetWise. If you want to store collected data when a vehicle loses connection with the cloud, use <code>TO_DISK</code>. If it's not specified, <code>OFF</code> is used.</p> <p>Default: <code>OFF</code> </p>"""
    compression: NotRequired["aws_sdk_iotfleetwise.types.compression.Compression"]
    """<p>Determines whether to compress signals before transmitting data to Amazon Web Services IoT FleetWise. If you don't want to compress the signals, use <code>OFF</code>. If it's not specified, <code>SNAPPY</code> is used. </p> <p>Default: <code>SNAPPY</code> </p>"""
    priority: NotRequired["aws_sdk_iotfleetwise.types.priority.priority"]
    """<p>A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet. A campaign with the lowest value is deployed to vehicles before any other campaigns. If it's not specified, <code>0</code> is used. </p> <p>Default: <code>0</code> </p>"""
    signals_to_collect: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_information_list.SignalInformationList"
    ]
    """<p>A list of information about signals to collect. </p> <note> <p>If you upload a signal as a condition in a data partition for a campaign, then those same signals must be included in <code>signalsToCollect</code>.</p> </note>"""
    collection_scheme: "aws_sdk_iotfleetwise.types.collection_scheme.CollectionScheme"
    """<p> The data collection scheme associated with the campaign. You can specify a scheme that collects data based on time or an event.</p>"""
    data_extra_dimensions: NotRequired[
        "aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list.DataExtraDimensionNodePathList"
    ]
    """<p>A list of vehicle attributes to associate with a campaign. </p> <p>Enrich the data with specified vehicle attributes. For example, add <code>make</code> and <code>model</code> to the campaign, and Amazon Web Services IoT FleetWise will associate the data with those attributes as dimensions in Amazon Timestream. You can then query the data against <code>make</code> and <code>model</code>.</p> <p>Default: An empty array</p>"""
    tags: NotRequired["aws_sdk_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the campaign.</p>"""
    data_destination_configs: NotRequired[
        "aws_sdk_iotfleetwise.types.data_destination_configs.DataDestinationConfigs"
    ]
    """<p>The destination where the campaign sends data. You can send data to an MQTT topic, or store it in Amazon S3 or Amazon Timestream.</p> <p>MQTT is the publish/subscribe messaging protocol used by Amazon Web Services IoT to communicate with your devices.</p> <p>Amazon S3 optimizes the cost of data storage and provides additional mechanisms to use vehicle data, such as data lakes, centralized data storage, data processing pipelines, and analytics. Amazon Web Services IoT FleetWise supports at-least-once file delivery to S3. Your vehicle data is stored on multiple Amazon Web Services IoT FleetWise servers for redundancy and high availability.</p> <p>You can use Amazon Timestream to access and analyze time series data, and Timestream to query vehicle data so that you can identify trends and patterns.</p>"""
    data_partitions: NotRequired[
        "aws_sdk_iotfleetwise.types.data_partitions.DataPartitions"
    ]
    """<p>The data partitions associated with the signals collected from the vehicle.</p>"""
    signals_to_fetch: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_fetch_information_list.SignalFetchInformationList"
    ]
    """<p>A list of information about signals to fetch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCampaignRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["signalCatalogArn"] = value["signal_catalog_arn"]
    out["targetArn"] = value["target_arn"]
    if "start_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["startTime"] = aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["start_time"]
        )
    if "expiry_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["expiryTime"] = aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["expiry_time"]
        )
    if "post_trigger_collection_duration" in value:
        out["postTriggerCollectionDuration"] = value["post_trigger_collection_duration"]
    if "diagnostics_mode" in value:
        import aws_sdk_iotfleetwise.types.diagnostics_mode

        out["diagnosticsMode"] = (
            aws_sdk_iotfleetwise.types.diagnostics_mode.serialize_aws_json_1_0(
                value["diagnostics_mode"]
            )
        )
    if "spooling_mode" in value:
        import aws_sdk_iotfleetwise.types.spooling_mode

        out["spoolingMode"] = (
            aws_sdk_iotfleetwise.types.spooling_mode.serialize_aws_json_1_0(
                value["spooling_mode"]
            )
        )
    if "compression" in value:
        import aws_sdk_iotfleetwise.types.compression

        out["compression"] = (
            aws_sdk_iotfleetwise.types.compression.serialize_aws_json_1_0(
                value["compression"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "signals_to_collect" in value:
        import aws_sdk_iotfleetwise.types.signal_information_list

        out["signalsToCollect"] = (
            aws_sdk_iotfleetwise.types.signal_information_list.serialize_aws_json_1_0(
                value["signals_to_collect"]
            )
        )
    import aws_sdk_iotfleetwise.types.collection_scheme

    out["collectionScheme"] = (
        aws_sdk_iotfleetwise.types.collection_scheme.serialize_aws_json_1_0(
            value["collection_scheme"]
        )
    )
    if "data_extra_dimensions" in value:
        import aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list

        out["dataExtraDimensions"] = (
            aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list.serialize_aws_json_1_0(
                value["data_extra_dimensions"]
            )
        )
    if "tags" in value:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "data_destination_configs" in value:
        import aws_sdk_iotfleetwise.types.data_destination_configs

        out["dataDestinationConfigs"] = (
            aws_sdk_iotfleetwise.types.data_destination_configs.serialize_aws_json_1_0(
                value["data_destination_configs"]
            )
        )
    if "data_partitions" in value:
        import aws_sdk_iotfleetwise.types.data_partitions

        out["dataPartitions"] = (
            aws_sdk_iotfleetwise.types.data_partitions.serialize_aws_json_1_0(
                value["data_partitions"]
            )
        )
    if "signals_to_fetch" in value:
        import aws_sdk_iotfleetwise.types.signal_fetch_information_list

        out["signalsToFetch"] = (
            aws_sdk_iotfleetwise.types.signal_fetch_information_list.serialize_aws_json_1_0(
                value["signals_to_fetch"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCampaignRequest:
    out: CreateCampaignRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "signalCatalogArn" in data:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    else:
        raise DeserializationError("CreateCampaignRequest.signal_catalog_arn required")
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("CreateCampaignRequest.target_arn required")
    if "startTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["start_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    if "expiryTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["expiry_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["expiryTime"]
            )
        )
    if "postTriggerCollectionDuration" in data:
        out["post_trigger_collection_duration"] = data["postTriggerCollectionDuration"]
    if "diagnosticsMode" in data:
        import aws_sdk_iotfleetwise.types.diagnostics_mode

        out["diagnostics_mode"] = (
            aws_sdk_iotfleetwise.types.diagnostics_mode.deserialize_aws_json_1_0(
                data["diagnosticsMode"]
            )
        )
    if "spoolingMode" in data:
        import aws_sdk_iotfleetwise.types.spooling_mode

        out["spooling_mode"] = (
            aws_sdk_iotfleetwise.types.spooling_mode.deserialize_aws_json_1_0(
                data["spoolingMode"]
            )
        )
    if "compression" in data:
        import aws_sdk_iotfleetwise.types.compression

        out["compression"] = (
            aws_sdk_iotfleetwise.types.compression.deserialize_aws_json_1_0(
                data["compression"]
            )
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    if "signalsToCollect" in data:
        import aws_sdk_iotfleetwise.types.signal_information_list

        out["signals_to_collect"] = (
            aws_sdk_iotfleetwise.types.signal_information_list.deserialize_aws_json_1_0(
                data["signalsToCollect"]
            )
        )
    if "collectionScheme" in data:
        import aws_sdk_iotfleetwise.types.collection_scheme

        out["collection_scheme"] = (
            aws_sdk_iotfleetwise.types.collection_scheme.deserialize_aws_json_1_0(
                data["collectionScheme"]
            )
        )
    else:
        raise DeserializationError("CreateCampaignRequest.collection_scheme required")
    if "dataExtraDimensions" in data:
        import aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list

        out["data_extra_dimensions"] = (
            aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list.deserialize_aws_json_1_0(
                data["dataExtraDimensions"]
            )
        )
    if "tags" in data:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "dataDestinationConfigs" in data:
        import aws_sdk_iotfleetwise.types.data_destination_configs

        out["data_destination_configs"] = (
            aws_sdk_iotfleetwise.types.data_destination_configs.deserialize_aws_json_1_0(
                data["dataDestinationConfigs"]
            )
        )
    if "dataPartitions" in data:
        import aws_sdk_iotfleetwise.types.data_partitions

        out["data_partitions"] = (
            aws_sdk_iotfleetwise.types.data_partitions.deserialize_aws_json_1_0(
                data["dataPartitions"]
            )
        )
    if "signalsToFetch" in data:
        import aws_sdk_iotfleetwise.types.signal_fetch_information_list

        out["signals_to_fetch"] = (
            aws_sdk_iotfleetwise.types.signal_fetch_information_list.deserialize_aws_json_1_0(
                data["signalsToFetch"]
            )
        )
    return out
