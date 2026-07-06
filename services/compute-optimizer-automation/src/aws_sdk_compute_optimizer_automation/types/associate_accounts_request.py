"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AssociateAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.account_id_list
    import aws_sdk_compute_optimizer_automation.types.client_token


class AssociateAccountsRequest(TypedDict, closed=True):
    account_ids: (
        "aws_sdk_compute_optimizer_automation.types.account_id_list.AccountIdList"
    )
    """<p> The IDs of the member accounts to associate. You can specify up to 50 account IDs. </p>"""
    client_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p> A unique identifier to ensure idempotency of the request. Valid for 24 hours after creation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateAccountsRequest) -> dict:
    out: dict = {}
    import aws_sdk_compute_optimizer_automation.types.account_id_list

    out["accountIds"] = (
        aws_sdk_compute_optimizer_automation.types.account_id_list.serialize_aws_json_1_0(
            value["account_ids"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateAccountsRequest:
    out: AssociateAccountsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_compute_optimizer_automation.types.account_id_list

        out["account_ids"] = (
            aws_sdk_compute_optimizer_automation.types.account_id_list.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    else:
        raise DeserializationError("AssociateAccountsRequest.account_ids required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
