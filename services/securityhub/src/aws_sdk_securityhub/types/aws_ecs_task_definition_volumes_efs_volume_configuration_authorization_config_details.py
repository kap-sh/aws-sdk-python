"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails(
    TypedDict, closed=True
):
    access_point_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon EFS access point identifier to use.</p>"""
    iam: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Whether to use the Amazon ECS task IAM role defined in a task definition when mounting the Amazon EFS file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails,
) -> dict:
    out: dict = {}
    if "access_point_id" in value:
        out["AccessPointId"] = value["access_point_id"]
    if "iam" in value:
        out["Iam"] = value["iam"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails:
    out: AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails = {}  # type: ignore[typeddict-item]
    if "AccessPointId" in data:
        out["access_point_id"] = data["AccessPointId"]
    if "Iam" in data:
        out["iam"] = data["Iam"]
    return out
