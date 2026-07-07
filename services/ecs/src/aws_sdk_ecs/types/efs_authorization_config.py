"""Generated from Smithy shape ``com.amazonaws.ecs#EFSAuthorizationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.efs_authorization_config_iam
    import aws_sdk_ecs.types.string


class EFSAuthorizationConfig(TypedDict, closed=True):
    access_point_id: NotRequired["aws_sdk_ecs.types.string.String"]
    r"""<p>The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the <code>EFSVolumeConfiguration</code> must either be omitted or set to <code>/</code> which will enforce the path set on the EFS access point. If an access point is used, transit encryption must be on in the <code>EFSVolumeConfiguration</code>. For more information, see <a href=\"https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html\">Working with Amazon EFS access points</a> in the <i>Amazon Elastic File System User Guide</i>.</p>"""
    iam: NotRequired[
        "aws_sdk_ecs.types.efs_authorization_config_iam.EFSAuthorizationConfigIAM"
    ]
    r"""<p>Determines whether to use the Amazon ECS task role defined in a task definition when mounting the Amazon EFS file system. If it is turned on, transit encryption must be turned on in the <code>EFSVolumeConfiguration</code>. If this parameter is omitted, the default value of <code>DISABLED</code> is used. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html#efs-volume-accesspoints\">Using Amazon EFS access points</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EFSAuthorizationConfig) -> dict:
    out: dict = {}
    if "access_point_id" in value:
        out["accessPointId"] = value["access_point_id"]
    if "iam" in value:
        import aws_sdk_ecs.types.efs_authorization_config_iam

        out["iam"] = (
            aws_sdk_ecs.types.efs_authorization_config_iam.serialize_aws_json_1_1(
                value["iam"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EFSAuthorizationConfig:
    out: EFSAuthorizationConfig = {}  # type: ignore[typeddict-item]
    if "accessPointId" in data:
        out["access_point_id"] = data["accessPointId"]
    if "iam" in data:
        import aws_sdk_ecs.types.efs_authorization_config_iam

        out["iam"] = (
            aws_sdk_ecs.types.efs_authorization_config_iam.deserialize_aws_json_1_1(
                data["iam"]
            )
        )
    return out
