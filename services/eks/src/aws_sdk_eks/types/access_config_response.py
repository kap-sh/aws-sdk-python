"""Generated from Smithy shape ``com.amazonaws.eks#AccessConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.authentication_mode
    import aws_sdk_eks.types.boxed_boolean


class AccessConfigResponse(TypedDict, closed=True):
    bootstrap_cluster_creator_admin_permissions: NotRequired[
        "aws_sdk_eks.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Specifies whether or not the cluster creator IAM principal was set as a cluster admin access entry during cluster creation time.</p>"""
    authentication_mode: NotRequired[
        "aws_sdk_eks.types.authentication_mode.AuthenticationMode"
    ]
    """<p>The current authentication mode of the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessConfigResponse) -> dict:
    out: dict = {}
    if "bootstrap_cluster_creator_admin_permissions" in value:
        out["bootstrapClusterCreatorAdminPermissions"] = value[
            "bootstrap_cluster_creator_admin_permissions"
        ]
    if "authentication_mode" in value:
        import aws_sdk_eks.types.authentication_mode

        out["authenticationMode"] = (
            aws_sdk_eks.types.authentication_mode.serialize_json(
                value["authentication_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccessConfigResponse:
    out: AccessConfigResponse = {}  # type: ignore[typeddict-item]
    if "bootstrapClusterCreatorAdminPermissions" in data:
        out["bootstrap_cluster_creator_admin_permissions"] = data[
            "bootstrapClusterCreatorAdminPermissions"
        ]
    if "authenticationMode" in data:
        import aws_sdk_eks.types.authentication_mode

        out["authentication_mode"] = (
            aws_sdk_eks.types.authentication_mode.deserialize_json(
                data["authenticationMode"]
            )
        )
    return out
