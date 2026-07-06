"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetPermissionsBoundaryForPermissionSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.permissions_boundary


class GetPermissionsBoundaryForPermissionSetResponse(TypedDict, closed=True):
    permissions_boundary: NotRequired[
        "aws_sdk_sso_admin.types.permissions_boundary.PermissionsBoundary"
    ]
    """<p>The permissions boundary attached to the specified permission set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetPermissionsBoundaryForPermissionSetResponse,
) -> dict:
    out: dict = {}
    if "permissions_boundary" in value:
        import aws_sdk_sso_admin.types.permissions_boundary

        out["PermissionsBoundary"] = (
            aws_sdk_sso_admin.types.permissions_boundary.serialize_aws_json_1_1(
                value["permissions_boundary"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetPermissionsBoundaryForPermissionSetResponse:
    out: GetPermissionsBoundaryForPermissionSetResponse = {}  # type: ignore[typeddict-item]
    if "PermissionsBoundary" in data:
        import aws_sdk_sso_admin.types.permissions_boundary

        out["permissions_boundary"] = (
            aws_sdk_sso_admin.types.permissions_boundary.deserialize_aws_json_1_1(
                data["PermissionsBoundary"]
            )
        )
    return out
