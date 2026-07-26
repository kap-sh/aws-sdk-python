"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreatePermissionSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.permission_set


class CreatePermissionSetResponse(TypedDict, closed=True):
    permission_set: NotRequired["capo_sso_admin.types.permission_set.PermissionSet"]
    """<p>Defines the level of access on an Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePermissionSetResponse) -> dict:
    out: dict = {}
    if "permission_set" in value:
        import capo_sso_admin.types.permission_set

        out["PermissionSet"] = (
            capo_sso_admin.types.permission_set.serialize_aws_json_1_1(
                value["permission_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePermissionSetResponse:
    out: CreatePermissionSetResponse = {}  # type: ignore[typeddict-item]
    if "PermissionSet" in data:
        import capo_sso_admin.types.permission_set

        out["permission_set"] = (
            capo_sso_admin.types.permission_set.deserialize_aws_json_1_1(
                data["PermissionSet"]
            )
        )
    return out
