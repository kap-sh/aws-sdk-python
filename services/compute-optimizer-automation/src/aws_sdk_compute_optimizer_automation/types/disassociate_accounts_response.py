"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#DisassociateAccountsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.account_id_list
    import aws_sdk_compute_optimizer_automation.types.string_list


class DisassociateAccountsResponse(TypedDict):
    account_ids: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.account_id_list.AccountIdList"
    ]
    """<p> The IDs of the member accounts that were successfully disassociated. </p>"""
    errors: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.string_list.StringList"
    ]
    """<p> Any errors that occurred during the disassociation process. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateAccountsResponse) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_compute_optimizer_automation.types.account_id_list

        out["accountIds"] = (
            aws_sdk_compute_optimizer_automation.types.account_id_list.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "errors" in value:
        import aws_sdk_compute_optimizer_automation.types.string_list

        out["errors"] = (
            aws_sdk_compute_optimizer_automation.types.string_list.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateAccountsResponse:
    out: DisassociateAccountsResponse = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_compute_optimizer_automation.types.account_id_list

        out["account_ids"] = (
            aws_sdk_compute_optimizer_automation.types.account_id_list.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if "errors" in data:
        import aws_sdk_compute_optimizer_automation.types.string_list

        out["errors"] = (
            aws_sdk_compute_optimizer_automation.types.string_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
