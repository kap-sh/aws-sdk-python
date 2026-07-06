"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.account_info_list
    import aws_sdk_compute_optimizer_automation.types.next_token


class ListAccountsResponse(TypedDict, closed=True):
    accounts: (
        "aws_sdk_compute_optimizer_automation.types.account_info_list.AccountInfoList"
    )
    """<p> The list of accounts in your organization enrolled in Compute Optimizer </p>"""
    next_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p> The token to use to retrieve the next page of results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAccountsResponse) -> dict:
    out: dict = {}
    import aws_sdk_compute_optimizer_automation.types.account_info_list

    out["accounts"] = (
        aws_sdk_compute_optimizer_automation.types.account_info_list.serialize_aws_json_1_0(
            value["accounts"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAccountsResponse:
    out: ListAccountsResponse = {}  # type: ignore[typeddict-item]
    if "accounts" in data:
        import aws_sdk_compute_optimizer_automation.types.account_info_list

        out["accounts"] = (
            aws_sdk_compute_optimizer_automation.types.account_info_list.deserialize_aws_json_1_0(
                data["accounts"]
            )
        )
    else:
        raise DeserializationError("ListAccountsResponse.accounts required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
