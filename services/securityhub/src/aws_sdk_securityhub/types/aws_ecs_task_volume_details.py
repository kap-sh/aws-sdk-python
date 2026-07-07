"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskVolumeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_volume_host_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskVolumeDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. This name is referenced in the <code>sourceVolume</code> parameter of container definition <code>mountPoints</code>. </p>"""
    host: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_task_volume_host_details.AwsEcsTaskVolumeHostDetails"
    ]
    """<p>This parameter is specified when you use bind mount host volumes. The contents of the <code>host</code> parameter determine whether your bind mount host volume persists on the host container instance and where it's stored. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskVolumeDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "host" in value:
        import aws_sdk_securityhub.types.aws_ecs_task_volume_host_details

        out["Host"] = (
            aws_sdk_securityhub.types.aws_ecs_task_volume_host_details.serialize_json(
                value["host"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEcsTaskVolumeDetails:
    out: AwsEcsTaskVolumeDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Host" in data:
        import aws_sdk_securityhub.types.aws_ecs_task_volume_host_details

        out["host"] = (
            aws_sdk_securityhub.types.aws_ecs_task_volume_host_details.deserialize_json(
                data["Host"]
            )
        )
    return out
