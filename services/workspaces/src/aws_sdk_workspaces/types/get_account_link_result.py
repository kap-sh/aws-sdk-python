"""Generated from Smithy shape ``com.amazonaws.workspaces#GetAccountLinkResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.account_link


class GetAccountLinkResult(TypedDict, closed=True):
    account_link: NotRequired["aws_sdk_workspaces.types.account_link.AccountLink"]
    """<p>The account link of the account link to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountLinkResult) -> dict:
    out: dict = {}
    if "account_link" in value:
        import aws_sdk_workspaces.types.account_link

        out["AccountLink"] = (
            aws_sdk_workspaces.types.account_link.serialize_aws_json_1_1(
                value["account_link"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountLinkResult:
    out: GetAccountLinkResult = {}  # type: ignore[typeddict-item]
    if "AccountLink" in data:
        import aws_sdk_workspaces.types.account_link

        out["account_link"] = (
            aws_sdk_workspaces.types.account_link.deserialize_aws_json_1_1(
                data["AccountLink"]
            )
        )
    return out
