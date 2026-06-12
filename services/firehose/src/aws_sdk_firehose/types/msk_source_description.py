"""Generated from Smithy shape ``com.amazonaws.firehose#MSKSourceDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.authentication_configuration
    import aws_sdk_firehose.types.delivery_start_timestamp
    import aws_sdk_firehose.types.msk_cluster_arn
    import aws_sdk_firehose.types.read_from_timestamp
    import aws_sdk_firehose.types.topic_name


class MSKSourceDescription(TypedDict):
    msk_cluster_arn: NotRequired["aws_sdk_firehose.types.msk_cluster_arn.MSKClusterARN"]
    """<p>The ARN of the Amazon MSK cluster.</p>"""
    topic_name: NotRequired["aws_sdk_firehose.types.topic_name.TopicName"]
    """<p>The topic name within the Amazon MSK cluster.</p>"""
    authentication_configuration: NotRequired[
        "aws_sdk_firehose.types.authentication_configuration.AuthenticationConfiguration"
    ]
    """<p>The authentication configuration of the Amazon MSK cluster.</p>"""
    delivery_start_timestamp: NotRequired[
        "aws_sdk_firehose.types.delivery_start_timestamp.DeliveryStartTimestamp"
    ]
    """<p>Firehose starts retrieving records from the topic within the Amazon MSK cluster starting with this timestamp.</p>"""
    read_from_timestamp: NotRequired[
        "aws_sdk_firehose.types.read_from_timestamp.ReadFromTimestamp"
    ]
    """<p>The start date and time in UTC for the offset position within your MSK topic from where Firehose begins to read. By default, this is set to timestamp when Firehose becomes Active. </p> <p>If you want to create a Firehose stream with Earliest start position from SDK or CLI, you need to set the <code>ReadFromTimestampUTC</code> parameter to Epoch (1970-01-01T00:00:00Z). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MSKSourceDescription) -> dict:
    out: dict = {}
    if "msk_cluster_arn" in value:
        out["MSKClusterARN"] = value["msk_cluster_arn"]
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    if "authentication_configuration" in value:
        import aws_sdk_firehose.types.authentication_configuration

        out["AuthenticationConfiguration"] = (
            aws_sdk_firehose.types.authentication_configuration.serialize_aws_json_1_1(
                value["authentication_configuration"]
            )
        )
    if "delivery_start_timestamp" in value:
        import aws_sdk_firehose.types.delivery_start_timestamp

        out["DeliveryStartTimestamp"] = (
            aws_sdk_firehose.types.delivery_start_timestamp.serialize_aws_json_1_1(
                value["delivery_start_timestamp"]
            )
        )
    if "read_from_timestamp" in value:
        import aws_sdk_firehose.types.read_from_timestamp

        out["ReadFromTimestamp"] = (
            aws_sdk_firehose.types.read_from_timestamp.serialize_aws_json_1_1(
                value["read_from_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MSKSourceDescription:
    out: MSKSourceDescription = {}  # type: ignore[typeddict-item]
    if "MSKClusterARN" in data:
        out["msk_cluster_arn"] = data["MSKClusterARN"]
    if "TopicName" in data:
        out["topic_name"] = data["TopicName"]
    if "AuthenticationConfiguration" in data:
        import aws_sdk_firehose.types.authentication_configuration

        out["authentication_configuration"] = (
            aws_sdk_firehose.types.authentication_configuration.deserialize_aws_json_1_1(
                data["AuthenticationConfiguration"]
            )
        )
    if "DeliveryStartTimestamp" in data:
        import aws_sdk_firehose.types.delivery_start_timestamp

        out["delivery_start_timestamp"] = (
            aws_sdk_firehose.types.delivery_start_timestamp.deserialize_aws_json_1_1(
                data["DeliveryStartTimestamp"]
            )
        )
    if "ReadFromTimestamp" in data:
        import aws_sdk_firehose.types.read_from_timestamp

        out["read_from_timestamp"] = (
            aws_sdk_firehose.types.read_from_timestamp.deserialize_aws_json_1_1(
                data["ReadFromTimestamp"]
            )
        )
    return out
