"""Generated from Smithy shape ``com.amazonaws.detective#BatchGetGraphMemberDatasourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.membership_datasources_list
    import capo_detective.types.unprocessed_account_list


class BatchGetGraphMemberDatasourcesResponse(TypedDict, closed=True):
    member_datasources: NotRequired[
        "capo_detective.types.membership_datasources_list.MembershipDatasourcesList"
    ]
    """<p>Details on the status of data source packages for members of the behavior graph.</p>"""
    unprocessed_accounts: NotRequired[
        "capo_detective.types.unprocessed_account_list.UnprocessedAccountList"
    ]
    """<p>Accounts that data source package information could not be retrieved for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetGraphMemberDatasourcesResponse) -> dict:
    out: dict = {}
    if "member_datasources" in value:
        import capo_detective.types.membership_datasources_list

        out["MemberDatasources"] = (
            capo_detective.types.membership_datasources_list.serialize_json(
                value["member_datasources"]
            )
        )
    if "unprocessed_accounts" in value:
        import capo_detective.types.unprocessed_account_list

        out["UnprocessedAccounts"] = (
            capo_detective.types.unprocessed_account_list.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetGraphMemberDatasourcesResponse:
    out: BatchGetGraphMemberDatasourcesResponse = {}  # type: ignore[typeddict-item]
    if "MemberDatasources" in data:
        import capo_detective.types.membership_datasources_list

        out["member_datasources"] = (
            capo_detective.types.membership_datasources_list.deserialize_json(
                data["MemberDatasources"]
            )
        )
    if "UnprocessedAccounts" in data:
        import capo_detective.types.unprocessed_account_list

        out["unprocessed_accounts"] = (
            capo_detective.types.unprocessed_account_list.deserialize_json(
                data["UnprocessedAccounts"]
            )
        )
    return out
