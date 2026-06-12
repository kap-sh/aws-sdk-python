"""Generated from Smithy shape ``com.amazonaws.detective#BatchGetGraphMemberDatasourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.membership_datasources_list
    import aws_sdk_detective.types.unprocessed_account_list


class BatchGetGraphMemberDatasourcesResponse(TypedDict):
    member_datasources: NotRequired[
        "aws_sdk_detective.types.membership_datasources_list.MembershipDatasourcesList"
    ]
    """<p>Details on the status of data source packages for members of the behavior graph.</p>"""
    unprocessed_accounts: NotRequired[
        "aws_sdk_detective.types.unprocessed_account_list.UnprocessedAccountList"
    ]
    """<p>Accounts that data source package information could not be retrieved for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetGraphMemberDatasourcesResponse) -> dict:
    out: dict = {}
    if "member_datasources" in value:
        import aws_sdk_detective.types.membership_datasources_list

        out["MemberDatasources"] = (
            aws_sdk_detective.types.membership_datasources_list.serialize_json(
                value["member_datasources"]
            )
        )
    if "unprocessed_accounts" in value:
        import aws_sdk_detective.types.unprocessed_account_list

        out["UnprocessedAccounts"] = (
            aws_sdk_detective.types.unprocessed_account_list.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetGraphMemberDatasourcesResponse:
    out: BatchGetGraphMemberDatasourcesResponse = {}  # type: ignore[typeddict-item]
    if "MemberDatasources" in data:
        import aws_sdk_detective.types.membership_datasources_list

        out["member_datasources"] = (
            aws_sdk_detective.types.membership_datasources_list.deserialize_json(
                data["MemberDatasources"]
            )
        )
    if "UnprocessedAccounts" in data:
        import aws_sdk_detective.types.unprocessed_account_list

        out["unprocessed_accounts"] = (
            aws_sdk_detective.types.unprocessed_account_list.deserialize_json(
                data["UnprocessedAccounts"]
            )
        )
    return out
