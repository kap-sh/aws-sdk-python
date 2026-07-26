"""Generated from Smithy shape ``com.amazonaws.inspector2#DisableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id_set
    import capo_inspector2.types.disable_resource_type_list


class DisableRequest(TypedDict, closed=True):
    account_ids: NotRequired["capo_inspector2.types.account_id_set.AccountIdSet"]
    """<p>An array of account IDs you want to disable Amazon Inspector scans for.</p>"""
    resource_types: NotRequired[
        "capo_inspector2.types.disable_resource_type_list.DisableResourceTypeList"
    ]
    """<p>The resource scan types you want to disable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_inspector2.types.account_id_set

        out["accountIds"] = capo_inspector2.types.account_id_set.serialize_json(
            value["account_ids"]
        )
    if "resource_types" in value:
        import capo_inspector2.types.disable_resource_type_list

        out["resourceTypes"] = (
            capo_inspector2.types.disable_resource_type_list.serialize_json(
                value["resource_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisableRequest:
    out: DisableRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import capo_inspector2.types.account_id_set

        out["account_ids"] = capo_inspector2.types.account_id_set.deserialize_json(
            data["accountIds"]
        )
    if "resourceTypes" in data:
        import capo_inspector2.types.disable_resource_type_list

        out["resource_types"] = (
            capo_inspector2.types.disable_resource_type_list.deserialize_json(
                data["resourceTypes"]
            )
        )
    return out
