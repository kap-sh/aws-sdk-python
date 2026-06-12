"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VolumeAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2VolumeAttachment(TypedDict):
    attach_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The datetime when the attachment initiated.</p>"""
    delete_on_termination: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the EBS volume is deleted when the EC2 instance is terminated.</p>"""
    instance_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the EC2 instance.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The attachment state of the volume. Valid values are as follows:</p> <ul> <li> <p> <code>attaching</code> </p> </li> <li> <p> <code>attached</code> </p> </li> <li> <p> <code>busy</code> </p> </li> <li> <p> <code>detaching</code> </p> </li> <li> <p> <code>detached</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VolumeAttachment) -> dict:
    out: dict = {}
    if "attach_time" in value:
        out["AttachTime"] = value["attach_time"]
    if "delete_on_termination" in value:
        out["DeleteOnTermination"] = value["delete_on_termination"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsEc2VolumeAttachment:
    out: AwsEc2VolumeAttachment = {}  # type: ignore[typeddict-item]
    if "AttachTime" in data:
        out["attach_time"] = data["AttachTime"]
    if "DeleteOnTermination" in data:
        out["delete_on_termination"] = data["DeleteOnTermination"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
