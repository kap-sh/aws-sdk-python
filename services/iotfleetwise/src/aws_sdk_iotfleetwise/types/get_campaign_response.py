"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetCampaignResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.campaign_arn
    import aws_sdk_iotfleetwise.types.campaign_name
    import aws_sdk_iotfleetwise.types.campaign_status
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
    import aws_sdk_iotfleetwise.types.timestamp
    import aws_sdk_iotfleetwise.types.uint32


class GetCampaignResponse(TypedDict):
    name: NotRequired["aws_sdk_iotfleetwise.types.campaign_name.campaignName"]
    """<p>The name of the campaign.</p>"""
    arn: NotRequired["aws_sdk_iotfleetwise.types.campaign_arn.campaignArn"]
    """<p> The Amazon Resource Name (ARN) of the campaign. </p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p>The description of the campaign.</p>"""
    signal_catalog_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p> The ARN of a signal catalog. </p>"""
    target_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p> The ARN of the vehicle or the fleet targeted by the campaign. </p>"""
    status: NotRequired["aws_sdk_iotfleetwise.types.campaign_status.CampaignStatus"]
    """<p>The state of the campaign. The status can be one of: <code>CREATING</code>, <code>WAITING_FOR_APPROVAL</code>, <code>RUNNING</code>, and <code>SUSPENDED</code>. </p>"""
    start_time: NotRequired["aws_sdk_iotfleetwise.types.timestamp.timestamp"]
    """<p> The time, in milliseconds, to deliver a campaign after it was approved.</p>"""
    expiry_time: NotRequired["aws_sdk_iotfleetwise.types.timestamp.timestamp"]
    """<p> The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time). Vehicle data won't be collected after the campaign expires.</p>"""
    post_trigger_collection_duration: NotRequired[
        "aws_sdk_iotfleetwise.types.uint32.uint32"
    ]
    """<p> How long (in seconds) to collect raw data after a triggering event initiates the collection. </p>"""
    diagnostics_mode: NotRequired[
        "aws_sdk_iotfleetwise.types.diagnostics_mode.DiagnosticsMode"
    ]
    """<p> Option for a vehicle to send diagnostic trouble codes to Amazon Web Services IoT FleetWise. </p>"""
    spooling_mode: NotRequired["aws_sdk_iotfleetwise.types.spooling_mode.SpoolingMode"]
    """<p> Whether to store collected data after a vehicle lost a connection with the cloud. After a connection is re-established, the data is automatically forwarded to Amazon Web Services IoT FleetWise. </p>"""
    compression: NotRequired["aws_sdk_iotfleetwise.types.compression.Compression"]
    """<p> Whether to compress signals before transmitting data to Amazon Web Services IoT FleetWise. If <code>OFF</code> is specified, the signals aren't compressed. If it's not specified, <code>SNAPPY</code> is used. </p>"""
    priority: NotRequired["aws_sdk_iotfleetwise.types.priority.priority"]
    """<p> A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet. A campaign with the lowest value is deployed to vehicles before any other campaigns.</p>"""
    signals_to_collect: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_information_list.SignalInformationList"
    ]
    """<p> Information about a list of signals to collect data on. </p>"""
    collection_scheme: NotRequired[
        "aws_sdk_iotfleetwise.types.collection_scheme.CollectionScheme"
    ]
    """<p> Information about the data collection scheme associated with the campaign. </p>"""
    data_extra_dimensions: NotRequired[
        "aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list.DataExtraDimensionNodePathList"
    ]
    """<p> A list of vehicle attributes associated with the campaign. </p>"""
    creation_time: NotRequired["aws_sdk_iotfleetwise.types.timestamp.timestamp"]
    """<p> The time the campaign was created in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: NotRequired[
        "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    ]
    """<p>The last time the campaign was modified.</p>"""
    data_destination_configs: NotRequired[
        "aws_sdk_iotfleetwise.types.data_destination_configs.DataDestinationConfigs"
    ]
    """<p>The destination where the campaign sends data. You can send data to an MQTT topic, or store it in Amazon S3 or Amazon Timestream.</p> <p>MQTT is the publish/subscribe messaging protocol used by Amazon Web Services IoT to communicate with your devices.</p> <p>Amazon S3 optimizes the cost of data storage and provides additional mechanisms to use vehicle data, such as data lakes, centralized data storage, data processing pipelines, and analytics. </p> <p>You can use Amazon Timestream to access and analyze time series data, and Timestream to query vehicle data so that you can identify trends and patterns.</p>"""
    data_partitions: NotRequired[
        "aws_sdk_iotfleetwise.types.data_partitions.DataPartitions"
    ]
    """<p>The data partitions associated with the signals collected from the vehicle.</p>"""
    signals_to_fetch: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_fetch_information_list.SignalFetchInformationList"
    ]
    """<p>Information about a list of signals to fetch data from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCampaignResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "signal_catalog_arn" in value:
        out["signalCatalogArn"] = value["signal_catalog_arn"]
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "status" in value:
        import aws_sdk_iotfleetwise.types.campaign_status

        out["status"] = (
            aws_sdk_iotfleetwise.types.campaign_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
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
    if "collection_scheme" in value:
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
    if "creation_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creationTime"] = (
            aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["creation_time"]
            )
        )
    if "last_modification_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["lastModificationTime"] = (
            aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["last_modification_time"]
            )
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


def deserialize_aws_json_1_0(data: dict) -> GetCampaignResponse:
    out: GetCampaignResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "description" in data:
        out["description"] = data["description"]
    if "signalCatalogArn" in data:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    if "status" in data:
        import aws_sdk_iotfleetwise.types.campaign_status

        out["status"] = (
            aws_sdk_iotfleetwise.types.campaign_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
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
    if "dataExtraDimensions" in data:
        import aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list

        out["data_extra_dimensions"] = (
            aws_sdk_iotfleetwise.types.data_extra_dimension_node_path_list.deserialize_aws_json_1_0(
                data["dataExtraDimensions"]
            )
        )
    if "creationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creation_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    if "lastModificationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
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
