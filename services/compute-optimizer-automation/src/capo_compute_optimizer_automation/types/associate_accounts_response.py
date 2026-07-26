"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AssociateAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.account_id_list
    import capo_compute_optimizer_automation.types.string_list


class AssociateAccountsResponse(TypedDict, closed=True):
    account_ids: NotRequired[
        "capo_compute_optimizer_automation.types.account_id_list.AccountIdList"
    ]
    """<p> The IDs of the member accounts that were successfully associated. </p>"""
    errors: NotRequired[
        "capo_compute_optimizer_automation.types.string_list.StringList"
    ]
    """<p> Any errors that occurred during the association process. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateAccountsResponse) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_compute_optimizer_automation.types.account_id_list

        out["accountIds"] = (
            capo_compute_optimizer_automation.types.account_id_list.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "errors" in value:
        import capo_compute_optimizer_automation.types.string_list

        out["errors"] = (
            capo_compute_optimizer_automation.types.string_list.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateAccountsResponse:
    out: AssociateAccountsResponse = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import capo_compute_optimizer_automation.types.account_id_list

        out["account_ids"] = (
            capo_compute_optimizer_automation.types.account_id_list.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if "errors" in data:
        import capo_compute_optimizer_automation.types.string_list

        out["errors"] = (
            capo_compute_optimizer_automation.types.string_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
