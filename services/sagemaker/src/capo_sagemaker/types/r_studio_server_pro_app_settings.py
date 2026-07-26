"""Generated from Smithy shape ``com.amazonaws.sagemaker#RStudioServerProAppSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.r_studio_server_pro_access_status
    import capo_sagemaker.types.r_studio_server_pro_user_group


class RStudioServerProAppSettings(TypedDict, closed=True):
    access_status: NotRequired[
        "capo_sagemaker.types.r_studio_server_pro_access_status.RStudioServerProAccessStatus"
    ]
    """<p>Indicates whether the current user has access to the <code>RStudioServerPro</code> app.</p>"""
    user_group: NotRequired[
        "capo_sagemaker.types.r_studio_server_pro_user_group.RStudioServerProUserGroup"
    ]
    """<p>The level of permissions that the user has within the <code>RStudioServerPro</code> app. This value defaults to `User`. The `Admin` value allows the user access to the RStudio Administrative Dashboard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RStudioServerProAppSettings) -> dict:
    out: dict = {}
    if "access_status" in value:
        import capo_sagemaker.types.r_studio_server_pro_access_status

        out["AccessStatus"] = (
            capo_sagemaker.types.r_studio_server_pro_access_status.serialize_aws_json_1_1(
                value["access_status"]
            )
        )
    if "user_group" in value:
        import capo_sagemaker.types.r_studio_server_pro_user_group

        out["UserGroup"] = (
            capo_sagemaker.types.r_studio_server_pro_user_group.serialize_aws_json_1_1(
                value["user_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RStudioServerProAppSettings:
    out: RStudioServerProAppSettings = {}  # type: ignore[typeddict-item]
    if "AccessStatus" in data:
        import capo_sagemaker.types.r_studio_server_pro_access_status

        out["access_status"] = (
            capo_sagemaker.types.r_studio_server_pro_access_status.deserialize_aws_json_1_1(
                data["AccessStatus"]
            )
        )
    if "UserGroup" in data:
        import capo_sagemaker.types.r_studio_server_pro_user_group

        out["user_group"] = (
            capo_sagemaker.types.r_studio_server_pro_user_group.deserialize_aws_json_1_1(
                data["UserGroup"]
            )
        )
    return out
