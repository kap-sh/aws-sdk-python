"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeStreamProcessorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.date_time
    import capo_rekognition.types.kms_key_id
    import capo_rekognition.types.regions_of_interest
    import capo_rekognition.types.role_arn
    import capo_rekognition.types.stream_processor_arn
    import capo_rekognition.types.stream_processor_data_sharing_preference
    import capo_rekognition.types.stream_processor_input
    import capo_rekognition.types.stream_processor_name
    import capo_rekognition.types.stream_processor_notification_channel
    import capo_rekognition.types.stream_processor_output
    import capo_rekognition.types.stream_processor_settings
    import capo_rekognition.types.stream_processor_status
    import capo_rekognition.types.string


class DescribeStreamProcessorResponse(TypedDict, closed=True):
    name: NotRequired[
        "capo_rekognition.types.stream_processor_name.StreamProcessorName"
    ]
    """<p>Name of the stream processor. </p>"""
    stream_processor_arn: NotRequired[
        "capo_rekognition.types.stream_processor_arn.StreamProcessorArn"
    ]
    """<p>ARN of the stream processor.</p>"""
    status: NotRequired[
        "capo_rekognition.types.stream_processor_status.StreamProcessorStatus"
    ]
    """<p>Current status of the stream processor.</p>"""
    status_message: NotRequired["capo_rekognition.types.string.String"]
    """<p>Detailed status message about the stream processor.</p>"""
    creation_timestamp: NotRequired["capo_rekognition.types.date_time.DateTime"]
    """<p>Date and time the stream processor was created</p>"""
    last_update_timestamp: NotRequired["capo_rekognition.types.date_time.DateTime"]
    """<p>The time, in Unix format, the stream processor was last updated. For example, when the stream processor moves from a running state to a failed state, or when the user starts or stops the stream processor.</p>"""
    input: NotRequired[
        "capo_rekognition.types.stream_processor_input.StreamProcessorInput"
    ]
    """<p>Kinesis video stream that provides the source streaming video.</p>"""
    output: NotRequired[
        "capo_rekognition.types.stream_processor_output.StreamProcessorOutput"
    ]
    """<p>Kinesis data stream to which Amazon Rekognition Video puts the analysis results.</p>"""
    role_arn: NotRequired["capo_rekognition.types.role_arn.RoleArn"]
    """<p>ARN of the IAM role that allows access to the stream processor.</p>"""
    settings: NotRequired[
        "capo_rekognition.types.stream_processor_settings.StreamProcessorSettings"
    ]
    """<p>Input parameters used in a streaming video analyzed by a stream processor. You can use <code>FaceSearch</code> to recognize faces in a streaming video, or you can use <code>ConnectedHome</code> to detect labels.</p>"""
    notification_channel: NotRequired[
        "capo_rekognition.types.stream_processor_notification_channel.StreamProcessorNotificationChannel"
    ]
    kms_key_id: NotRequired["capo_rekognition.types.kms_key_id.KmsKeyId"]
    """<p> The identifier for your AWS Key Management Service key (AWS KMS key). This is an optional parameter for label detection stream processors. </p>"""
    regions_of_interest: NotRequired[
        "capo_rekognition.types.regions_of_interest.RegionsOfInterest"
    ]
    """<p> Specifies locations in the frames where Amazon Rekognition checks for objects or people. This is an optional parameter for label detection stream processors. </p>"""
    data_sharing_preference: NotRequired[
        "capo_rekognition.types.stream_processor_data_sharing_preference.StreamProcessorDataSharingPreference"
    ]
    """<p> Shows whether you are sharing data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStreamProcessorResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "stream_processor_arn" in value:
        out["StreamProcessorArn"] = value["stream_processor_arn"]
    if "status" in value:
        import capo_rekognition.types.stream_processor_status

        out["Status"] = (
            capo_rekognition.types.stream_processor_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "creation_timestamp" in value:
        import capo_rekognition.types.date_time

        out["CreationTimestamp"] = (
            capo_rekognition.types.date_time.serialize_aws_json_1_1(
                value["creation_timestamp"]
            )
        )
    if "last_update_timestamp" in value:
        import capo_rekognition.types.date_time

        out["LastUpdateTimestamp"] = (
            capo_rekognition.types.date_time.serialize_aws_json_1_1(
                value["last_update_timestamp"]
            )
        )
    if "input" in value:
        import capo_rekognition.types.stream_processor_input

        out["Input"] = (
            capo_rekognition.types.stream_processor_input.serialize_aws_json_1_1(
                value["input"]
            )
        )
    if "output" in value:
        import capo_rekognition.types.stream_processor_output

        out["Output"] = (
            capo_rekognition.types.stream_processor_output.serialize_aws_json_1_1(
                value["output"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "settings" in value:
        import capo_rekognition.types.stream_processor_settings

        out["Settings"] = (
            capo_rekognition.types.stream_processor_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "notification_channel" in value:
        import capo_rekognition.types.stream_processor_notification_channel

        out["NotificationChannel"] = (
            capo_rekognition.types.stream_processor_notification_channel.serialize_aws_json_1_1(
                value["notification_channel"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "regions_of_interest" in value:
        import capo_rekognition.types.regions_of_interest

        out["RegionsOfInterest"] = (
            capo_rekognition.types.regions_of_interest.serialize_aws_json_1_1(
                value["regions_of_interest"]
            )
        )
    if "data_sharing_preference" in value:
        import capo_rekognition.types.stream_processor_data_sharing_preference

        out["DataSharingPreference"] = (
            capo_rekognition.types.stream_processor_data_sharing_preference.serialize_aws_json_1_1(
                value["data_sharing_preference"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStreamProcessorResponse:
    out: DescribeStreamProcessorResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "StreamProcessorArn" in data:
        out["stream_processor_arn"] = data["StreamProcessorArn"]
    if "Status" in data:
        import capo_rekognition.types.stream_processor_status

        out["status"] = (
            capo_rekognition.types.stream_processor_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "CreationTimestamp" in data:
        import capo_rekognition.types.date_time

        out["creation_timestamp"] = (
            capo_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CreationTimestamp"]
            )
        )
    if "LastUpdateTimestamp" in data:
        import capo_rekognition.types.date_time

        out["last_update_timestamp"] = (
            capo_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["LastUpdateTimestamp"]
            )
        )
    if "Input" in data:
        import capo_rekognition.types.stream_processor_input

        out["input"] = (
            capo_rekognition.types.stream_processor_input.deserialize_aws_json_1_1(
                data["Input"]
            )
        )
    if "Output" in data:
        import capo_rekognition.types.stream_processor_output

        out["output"] = (
            capo_rekognition.types.stream_processor_output.deserialize_aws_json_1_1(
                data["Output"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Settings" in data:
        import capo_rekognition.types.stream_processor_settings

        out["settings"] = (
            capo_rekognition.types.stream_processor_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if "NotificationChannel" in data:
        import capo_rekognition.types.stream_processor_notification_channel

        out["notification_channel"] = (
            capo_rekognition.types.stream_processor_notification_channel.deserialize_aws_json_1_1(
                data["NotificationChannel"]
            )
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "RegionsOfInterest" in data:
        import capo_rekognition.types.regions_of_interest

        out["regions_of_interest"] = (
            capo_rekognition.types.regions_of_interest.deserialize_aws_json_1_1(
                data["RegionsOfInterest"]
            )
        )
    if "DataSharingPreference" in data:
        import capo_rekognition.types.stream_processor_data_sharing_preference

        out["data_sharing_preference"] = (
            capo_rekognition.types.stream_processor_data_sharing_preference.deserialize_aws_json_1_1(
                data["DataSharingPreference"]
            )
        )
    return out
