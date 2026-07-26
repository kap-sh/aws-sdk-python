"""Generated from Smithy shape ``com.amazonaws.workmail#CreateImpersonationRoleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.impersonation_role_id


class CreateImpersonationRoleResponse(TypedDict, closed=True):
    impersonation_role_id: NotRequired[
        "capo_workmail.types.impersonation_role_id.ImpersonationRoleId"
    ]
    """<p>The new impersonation role ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImpersonationRoleResponse) -> dict:
    out: dict = {}
    if "impersonation_role_id" in value:
        out["ImpersonationRoleId"] = value["impersonation_role_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImpersonationRoleResponse:
    out: CreateImpersonationRoleResponse = {}  # type: ignore[typeddict-item]
    if "ImpersonationRoleId" in data:
        out["impersonation_role_id"] = data["ImpersonationRoleId"]
    return out
