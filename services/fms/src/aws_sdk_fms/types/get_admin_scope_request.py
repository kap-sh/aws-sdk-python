"""Generated from Smithy shape ``com.amazonaws.fms#GetAdminScopeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_account_id


class GetAdminScopeRequest(TypedDict):
    admin_account: "aws_sdk_fms.types.aws_account_id.AWSAccountId"
    """<p>The administrator account that you want to get the details for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdminScopeRequest) -> dict:
    out: dict = {}
    out["AdminAccount"] = value["admin_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdminScopeRequest:
    out: GetAdminScopeRequest = {}  # type: ignore[typeddict-item]
    if "AdminAccount" in data:
        out["admin_account"] = data["AdminAccount"]
    else:
        raise DeserializationError("GetAdminScopeRequest.admin_account required")
    return out
