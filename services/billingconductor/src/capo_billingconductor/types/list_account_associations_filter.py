"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListAccountAssociationsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.account_id
    import capo_billingconductor.types.account_id_filter_list
    import capo_billingconductor.types.association


class ListAccountAssociationsFilter(TypedDict, closed=True):
    association: NotRequired["capo_billingconductor.types.association.Association"]
    """<p> <code>MONITORED</code>: linked accounts that are associated to billing groups.</p> <p> <code>UNMONITORED</code>: linked accounts that are not associated to billing groups.</p> <p> <code>Billing Group Arn</code>: linked accounts that are associated to the provided Billing Group Arn.</p>"""
    account_id: NotRequired["capo_billingconductor.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID to filter on.</p>"""
    account_ids: NotRequired[
        "capo_billingconductor.types.account_id_filter_list.AccountIdFilterList"
    ]
    """<p> The list of Amazon Web Services IDs to retrieve their associated billing group for a given time range. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountAssociationsFilter) -> dict:
    out: dict = {}
    if "association" in value:
        out["Association"] = value["association"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "account_ids" in value:
        import capo_billingconductor.types.account_id_filter_list

        out["AccountIds"] = (
            capo_billingconductor.types.account_id_filter_list.serialize_json(
                value["account_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListAccountAssociationsFilter:
    out: ListAccountAssociationsFilter = {}  # type: ignore[typeddict-item]
    if "Association" in data:
        out["association"] = data["Association"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "AccountIds" in data:
        import capo_billingconductor.types.account_id_filter_list

        out["account_ids"] = (
            capo_billingconductor.types.account_id_filter_list.deserialize_json(
                data["AccountIds"]
            )
        )
    return out
