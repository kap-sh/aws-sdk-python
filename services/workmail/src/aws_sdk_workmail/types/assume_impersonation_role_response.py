"""Generated from Smithy shape ``com.amazonaws.workmail#AssumeImpersonationRoleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.expires_in
    import aws_sdk_workmail.types.impersonation_token


class AssumeImpersonationRoleResponse(TypedDict):
    token: NotRequired["aws_sdk_workmail.types.impersonation_token.ImpersonationToken"]
    """<p>The authentication token for the impersonation role.</p>"""
    expires_in: NotRequired["aws_sdk_workmail.types.expires_in.ExpiresIn"]
    """<p>The authentication token's validity, in seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssumeImpersonationRoleResponse) -> dict:
    out: dict = {}
    if "token" in value:
        out["Token"] = value["token"]
    if "expires_in" in value:
        out["ExpiresIn"] = value["expires_in"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssumeImpersonationRoleResponse:
    out: AssumeImpersonationRoleResponse = {}  # type: ignore[typeddict-item]
    if "Token" in data:
        out["token"] = data["Token"]
    if "ExpiresIn" in data:
        out["expires_in"] = data["ExpiresIn"]
    return out
