"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.boolean_object
    import aws_sdk_firehose.types.delivery_stream_arn
    import aws_sdk_firehose.types.delivery_stream_encryption_configuration
    import aws_sdk_firehose.types.delivery_stream_name
    import aws_sdk_firehose.types.delivery_stream_status
    import aws_sdk_firehose.types.delivery_stream_type
    import aws_sdk_firehose.types.delivery_stream_version_id
    import aws_sdk_firehose.types.destination_description_list
    import aws_sdk_firehose.types.failure_description
    import aws_sdk_firehose.types.source_description
    import aws_sdk_firehose.types.timestamp


class DeliveryStreamDescription(TypedDict, closed=True):
    delivery_stream_name: (
        "aws_sdk_firehose.types.delivery_stream_name.DeliveryStreamName"
    )
    """<p>The name of the Firehose stream.</p>"""
    delivery_stream_arn: "aws_sdk_firehose.types.delivery_stream_arn.DeliveryStreamARN"
    r"""<p>The Amazon Resource Name (ARN) of the Firehose stream. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    delivery_stream_status: (
        "aws_sdk_firehose.types.delivery_stream_status.DeliveryStreamStatus"
    )
    """<p>The status of the Firehose stream. If the status of a Firehose stream is <code>CREATING_FAILED</code>, this status doesn't change, and you can't invoke <code>CreateDeliveryStream</code> again on it. However, you can invoke the <a>DeleteDeliveryStream</a> operation to delete it.</p>"""
    failure_description: NotRequired[
        "aws_sdk_firehose.types.failure_description.FailureDescription"
    ]
    """<p>Provides details in case one of the following operations fails due to an error related to KMS: <a>CreateDeliveryStream</a>, <a>DeleteDeliveryStream</a>, <a>StartDeliveryStreamEncryption</a>, <a>StopDeliveryStreamEncryption</a>.</p>"""
    delivery_stream_encryption_configuration: NotRequired[
        "aws_sdk_firehose.types.delivery_stream_encryption_configuration.DeliveryStreamEncryptionConfiguration"
    ]
    """<p>Indicates the server-side encryption (SSE) status for the Firehose stream.</p>"""
    delivery_stream_type: (
        "aws_sdk_firehose.types.delivery_stream_type.DeliveryStreamType"
    )
    """<p>The Firehose stream type. This can be one of the following values:</p> <ul> <li> <p> <code>DirectPut</code>: Provider applications access the Firehose stream directly.</p> </li> <li> <p> <code>KinesisStreamAsSource</code>: The Firehose stream uses a Kinesis data stream as a source.</p> </li> </ul>"""
    version_id: (
        "aws_sdk_firehose.types.delivery_stream_version_id.DeliveryStreamVersionId"
    )
    """<p>Each time the destination is updated for a Firehose stream, the version ID is changed, and the current version ID is required when updating the destination. This is so that the service knows it is applying the changes to the correct version of the delivery stream.</p>"""
    create_timestamp: NotRequired["aws_sdk_firehose.types.timestamp.Timestamp"]
    """<p>The date and time that the Firehose stream was created.</p>"""
    last_update_timestamp: NotRequired["aws_sdk_firehose.types.timestamp.Timestamp"]
    """<p>The date and time that the Firehose stream was last updated.</p>"""
    source: NotRequired["aws_sdk_firehose.types.source_description.SourceDescription"]
    """<p>If the <code>DeliveryStreamType</code> parameter is <code>KinesisStreamAsSource</code>, a <a>SourceDescription</a> object describing the source Kinesis data stream.</p>"""
    destinations: (
        "aws_sdk_firehose.types.destination_description_list.DestinationDescriptionList"
    )
    """<p>The destinations.</p>"""
    has_more_destinations: "aws_sdk_firehose.types.boolean_object.BooleanObject"
    """<p>Indicates whether there are more destinations available to list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryStreamDescription) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    out["DeliveryStreamARN"] = value["delivery_stream_arn"]
    import aws_sdk_firehose.types.delivery_stream_status

    out["DeliveryStreamStatus"] = (
        aws_sdk_firehose.types.delivery_stream_status.serialize_aws_json_1_1(
            value["delivery_stream_status"]
        )
    )
    if "failure_description" in value:
        import aws_sdk_firehose.types.failure_description

        out["FailureDescription"] = (
            aws_sdk_firehose.types.failure_description.serialize_aws_json_1_1(
                value["failure_description"]
            )
        )
    if "delivery_stream_encryption_configuration" in value:
        import aws_sdk_firehose.types.delivery_stream_encryption_configuration

        out["DeliveryStreamEncryptionConfiguration"] = (
            aws_sdk_firehose.types.delivery_stream_encryption_configuration.serialize_aws_json_1_1(
                value["delivery_stream_encryption_configuration"]
            )
        )
    import aws_sdk_firehose.types.delivery_stream_type

    out["DeliveryStreamType"] = (
        aws_sdk_firehose.types.delivery_stream_type.serialize_aws_json_1_1(
            value["delivery_stream_type"]
        )
    )
    out["VersionId"] = value["version_id"]
    if "create_timestamp" in value:
        import aws_sdk_firehose.types.timestamp

        out["CreateTimestamp"] = (
            aws_sdk_firehose.types.timestamp.serialize_aws_json_1_1(
                value["create_timestamp"]
            )
        )
    if "last_update_timestamp" in value:
        import aws_sdk_firehose.types.timestamp

        out["LastUpdateTimestamp"] = (
            aws_sdk_firehose.types.timestamp.serialize_aws_json_1_1(
                value["last_update_timestamp"]
            )
        )
    if "source" in value:
        import aws_sdk_firehose.types.source_description

        out["Source"] = (
            aws_sdk_firehose.types.source_description.serialize_aws_json_1_1(
                value["source"]
            )
        )
    import aws_sdk_firehose.types.destination_description_list

    out["Destinations"] = (
        aws_sdk_firehose.types.destination_description_list.serialize_aws_json_1_1(
            value["destinations"]
        )
    )
    out["HasMoreDestinations"] = value["has_more_destinations"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliveryStreamDescription:
    out: DeliveryStreamDescription = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamName" in data:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError(
            "DeliveryStreamDescription.delivery_stream_name required"
        )
    if "DeliveryStreamARN" in data:
        out["delivery_stream_arn"] = data["DeliveryStreamARN"]
    else:
        raise DeserializationError(
            "DeliveryStreamDescription.delivery_stream_arn required"
        )
    if "DeliveryStreamStatus" in data:
        import aws_sdk_firehose.types.delivery_stream_status

        out["delivery_stream_status"] = (
            aws_sdk_firehose.types.delivery_stream_status.deserialize_aws_json_1_1(
                data["DeliveryStreamStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeliveryStreamDescription.delivery_stream_status required"
        )
    if "FailureDescription" in data:
        import aws_sdk_firehose.types.failure_description

        out["failure_description"] = (
            aws_sdk_firehose.types.failure_description.deserialize_aws_json_1_1(
                data["FailureDescription"]
            )
        )
    if "DeliveryStreamEncryptionConfiguration" in data:
        import aws_sdk_firehose.types.delivery_stream_encryption_configuration

        out["delivery_stream_encryption_configuration"] = (
            aws_sdk_firehose.types.delivery_stream_encryption_configuration.deserialize_aws_json_1_1(
                data["DeliveryStreamEncryptionConfiguration"]
            )
        )
    if "DeliveryStreamType" in data:
        import aws_sdk_firehose.types.delivery_stream_type

        out["delivery_stream_type"] = (
            aws_sdk_firehose.types.delivery_stream_type.deserialize_aws_json_1_1(
                data["DeliveryStreamType"]
            )
        )
    else:
        raise DeserializationError(
            "DeliveryStreamDescription.delivery_stream_type required"
        )
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    else:
        raise DeserializationError("DeliveryStreamDescription.version_id required")
    if "CreateTimestamp" in data:
        import aws_sdk_firehose.types.timestamp

        out["create_timestamp"] = (
            aws_sdk_firehose.types.timestamp.deserialize_aws_json_1_1(
                data["CreateTimestamp"]
            )
        )
    if "LastUpdateTimestamp" in data:
        import aws_sdk_firehose.types.timestamp

        out["last_update_timestamp"] = (
            aws_sdk_firehose.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdateTimestamp"]
            )
        )
    if "Source" in data:
        import aws_sdk_firehose.types.source_description

        out["source"] = (
            aws_sdk_firehose.types.source_description.deserialize_aws_json_1_1(
                data["Source"]
            )
        )
    if "Destinations" in data:
        import aws_sdk_firehose.types.destination_description_list

        out["destinations"] = (
            aws_sdk_firehose.types.destination_description_list.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    else:
        raise DeserializationError("DeliveryStreamDescription.destinations required")
    if "HasMoreDestinations" in data:
        out["has_more_destinations"] = data["HasMoreDestinations"]
    else:
        raise DeserializationError(
            "DeliveryStreamDescription.has_more_destinations required"
        )
    return out
