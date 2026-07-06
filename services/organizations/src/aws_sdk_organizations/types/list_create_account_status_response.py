"""Generated from Smithy shape ``com.amazonaws.organizations#ListCreateAccountStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.create_account_statuses
    import aws_sdk_organizations.types.next_token


class ListCreateAccountStatusResponse(TypedDict, closed=True):
    create_account_statuses: NotRequired[
        "aws_sdk_organizations.types.create_account_statuses.CreateAccountStatuses"
    ]
    """<p>A list of objects with details about the requests. Certain elements, such as the accountId number, are present in the output only after the account has been successfully created.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCreateAccountStatusResponse) -> dict:
    out: dict = {}
    if "create_account_statuses" in value:
        import aws_sdk_organizations.types.create_account_statuses

        out["CreateAccountStatuses"] = (
            aws_sdk_organizations.types.create_account_statuses.serialize_aws_json_1_1(
                value["create_account_statuses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCreateAccountStatusResponse:
    out: ListCreateAccountStatusResponse = {}  # type: ignore[typeddict-item]
    if "CreateAccountStatuses" in data:
        import aws_sdk_organizations.types.create_account_statuses

        out["create_account_statuses"] = (
            aws_sdk_organizations.types.create_account_statuses.deserialize_aws_json_1_1(
                data["CreateAccountStatuses"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
