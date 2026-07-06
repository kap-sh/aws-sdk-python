"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsContainerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_mount_point_list
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsContainerDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the container. </p>"""
    image: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The image used for the container. </p>"""
    mount_points: NotRequired[
        "aws_sdk_securityhub.types.aws_mount_point_list.AwsMountPointList"
    ]
    """<p>The mount points for data volumes in your container. </p>"""
    privileged: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsContainerDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "image" in value:
        out["Image"] = value["image"]
    if "mount_points" in value:
        import aws_sdk_securityhub.types.aws_mount_point_list

        out["MountPoints"] = (
            aws_sdk_securityhub.types.aws_mount_point_list.serialize_json(
                value["mount_points"]
            )
        )
    if "privileged" in value:
        out["Privileged"] = value["privileged"]
    return out


def deserialize_json(data: dict) -> AwsEcsContainerDetails:
    out: AwsEcsContainerDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Image" in data:
        out["image"] = data["Image"]
    if "MountPoints" in data:
        import aws_sdk_securityhub.types.aws_mount_point_list

        out["mount_points"] = (
            aws_sdk_securityhub.types.aws_mount_point_list.deserialize_json(
                data["MountPoints"]
            )
        )
    if "Privileged" in data:
        out["privileged"] = data["Privileged"]
    return out
