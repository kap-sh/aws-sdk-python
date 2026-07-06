"""Generated from Smithy shape ``com.amazonaws.sso#GetRoleCredentialsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso.types.role_credentials


class GetRoleCredentialsResponse(TypedDict, closed=True):
    role_credentials: NotRequired["aws_sdk_sso.types.role_credentials.RoleCredentials"]
    """<p>The credentials for the role that is assigned to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRoleCredentialsResponse) -> dict:
    out: dict = {}
    if "role_credentials" in value:
        import aws_sdk_sso.types.role_credentials

        out["roleCredentials"] = aws_sdk_sso.types.role_credentials.serialize_json(
            value["role_credentials"]
        )
    return out


def deserialize_json(data: dict) -> GetRoleCredentialsResponse:
    out: GetRoleCredentialsResponse = {}  # type: ignore[typeddict-item]
    if "roleCredentials" in data:
        import aws_sdk_sso.types.role_credentials

        out["role_credentials"] = aws_sdk_sso.types.role_credentials.deserialize_json(
            data["roleCredentials"]
        )
    return out
