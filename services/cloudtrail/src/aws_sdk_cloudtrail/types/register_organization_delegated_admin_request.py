"""Generated from Smithy shape ``com.amazonaws.cloudtrail#RegisterOrganizationDelegatedAdminRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.account_id


class RegisterOrganizationDelegatedAdminRequest(TypedDict):
    member_account_id: "aws_sdk_cloudtrail.types.account_id.AccountId"
    """<p>An organization member account ID that you want to designate as a delegated administrator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterOrganizationDelegatedAdminRequest) -> dict:
    out: dict = {}
    out["MemberAccountId"] = value["member_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterOrganizationDelegatedAdminRequest:
    out: RegisterOrganizationDelegatedAdminRequest = {}  # type: ignore[typeddict-item]
    if "MemberAccountId" in data:
        out["member_account_id"] = data["MemberAccountId"]
    else:
        raise DeserializationError(
            "RegisterOrganizationDelegatedAdminRequest.member_account_id required"
        )
    return out
