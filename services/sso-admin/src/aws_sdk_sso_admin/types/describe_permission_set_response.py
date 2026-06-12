"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribePermissionSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.permission_set


class DescribePermissionSetResponse(TypedDict):
    permission_set: NotRequired["aws_sdk_sso_admin.types.permission_set.PermissionSet"]
    """<p>Describes the level of access on an Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePermissionSetResponse) -> dict:
    out: dict = {}
    if "permission_set" in value:
        import aws_sdk_sso_admin.types.permission_set

        out["PermissionSet"] = (
            aws_sdk_sso_admin.types.permission_set.serialize_aws_json_1_1(
                value["permission_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePermissionSetResponse:
    out: DescribePermissionSetResponse = {}  # type: ignore[typeddict-item]
    if "PermissionSet" in data:
        import aws_sdk_sso_admin.types.permission_set

        out["permission_set"] = (
            aws_sdk_sso_admin.types.permission_set.deserialize_aws_json_1_1(
                data["PermissionSet"]
            )
        )
    return out
