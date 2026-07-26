"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VolumeAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_volume_attachment

AwsEc2VolumeAttachmentList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_volume_attachment.AwsEc2VolumeAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VolumeAttachmentList) -> list:
    import capo_securityhub.types.aws_ec2_volume_attachment

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_volume_attachment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsEc2VolumeAttachmentList:
    import capo_securityhub.types.aws_ec2_volume_attachment

    out: AwsEc2VolumeAttachmentList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_volume_attachment.deserialize_json(item)
        )
    return out
