"""Generated from Smithy shape ``com.amazonaws.ecs#EFSAuthorizationConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.efs_authorization_config_iam
    import aws_sdk_ecs.types.string


class EFSAuthorizationConfig(TypedDict):
    access_point_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the <code>EFSVolumeConfiguration</code> must either be omitted or set to <code>/</code> which will enforce the path set on the EFS access point. If an access point is used, transit encryption must be on in the <code>EFSVolumeConfiguration</code>. For more information, see <a href=\"https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html\">Working with Amazon EFS access points</a> in the <i>Amazon Elastic File System User Guide</i>.</p>"""
    iam: NotRequired[
        "aws_sdk_ecs.types.efs_authorization_config_iam.EFSAuthorizationConfigIAM"
    ]
    """<p>Determines whether to use the Amazon ECS task role defined in a task definition when mounting the Amazon EFS file system. If it is turned on, transit encryption must be turned on in the <code>EFSVolumeConfiguration</code>. If this parameter is omitted, the default value of <code>DISABLED</code> is used. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html#efs-volume-accesspoints\">Using Amazon EFS access points</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
