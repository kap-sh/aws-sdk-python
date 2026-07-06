"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentInfoDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.ec2_instance_id
    import aws_sdk_elastic_beanstalk.types.environment_info_type
    import aws_sdk_elastic_beanstalk.types.message
    import aws_sdk_elastic_beanstalk.types.sample_timestamp


class EnvironmentInfoDescription(TypedDict, closed=True):
    info_type: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_info_type.EnvironmentInfoType"
    ]
    """<p>The type of information retrieved.</p>"""
    ec2_instance_id: NotRequired[
        "aws_sdk_elastic_beanstalk.types.ec2_instance_id.Ec2InstanceId"
    ]
    """<p>The Amazon EC2 Instance ID for this information.</p>"""
    sample_timestamp: NotRequired[
        "aws_sdk_elastic_beanstalk.types.sample_timestamp.SampleTimestamp"
    ]
    """<p>The time stamp when this information was retrieved.</p>"""
    message: NotRequired["aws_sdk_elastic_beanstalk.types.message.Message"]
    """<p>The retrieved information. Currently contains a presigned Amazon S3 URL. The files are deleted after 15 minutes.</p> <p>Anyone in possession of this URL can access the files before they are deleted. Make the URL available only to trusted parties.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentInfoDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "info_type" in value:
        import aws_sdk_elastic_beanstalk.types.environment_info_type

        aws_sdk_elastic_beanstalk.types.environment_info_type.serialize_query(
            value["info_type"], pairs, f"{prefix}.InfoType"
        )
    if "ec2_instance_id" in value:
        pairs.append((f"{prefix}.Ec2InstanceId", str(value["ec2_instance_id"])))
    if "sample_timestamp" in value:
        import aws_sdk_elastic_beanstalk.types.sample_timestamp

        aws_sdk_elastic_beanstalk.types.sample_timestamp.serialize_query(
            value["sample_timestamp"], pairs, f"{prefix}.SampleTimestamp"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> EnvironmentInfoDescription:
    out: EnvironmentInfoDescription = {}  # type: ignore[typeddict-item]
    child_info_type = el.find("InfoType")
    if child_info_type is not None:
        import aws_sdk_elastic_beanstalk.types.environment_info_type

        out["info_type"] = (
            aws_sdk_elastic_beanstalk.types.environment_info_type.deserialize_query(
                child_info_type
            )
        )
    child_ec2_instance_id = el.find("Ec2InstanceId")
    if child_ec2_instance_id is not None:
        out["ec2_instance_id"] = str(child_ec2_instance_id.text or "")
    child_sample_timestamp = el.find("SampleTimestamp")
    if child_sample_timestamp is not None:
        import aws_sdk_elastic_beanstalk.types.sample_timestamp

        out["sample_timestamp"] = (
            aws_sdk_elastic_beanstalk.types.sample_timestamp.deserialize_query(
                child_sample_timestamp
            )
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
