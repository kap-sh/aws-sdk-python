"""Generated from Smithy shape ``com.amazonaws.organizations#CreateGovCloudAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.create_account_status


class CreateGovCloudAccountResponse(TypedDict, closed=True):
    create_account_status: NotRequired[
        "capo_organizations.types.create_account_status.CreateAccountStatus"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGovCloudAccountResponse) -> dict:
    out: dict = {}
    if "create_account_status" in value:
        import capo_organizations.types.create_account_status

        out["CreateAccountStatus"] = (
            capo_organizations.types.create_account_status.serialize_aws_json_1_1(
                value["create_account_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGovCloudAccountResponse:
    out: CreateGovCloudAccountResponse = {}  # type: ignore[typeddict-item]
    if "CreateAccountStatus" in data:
        import capo_organizations.types.create_account_status

        out["create_account_status"] = (
            capo_organizations.types.create_account_status.deserialize_aws_json_1_1(
                data["CreateAccountStatus"]
            )
        )
    return out
