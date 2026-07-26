"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeOrganizationHealthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.account_id_list
    import capo_devops_guru.types.organizational_unit_id_list


class DescribeOrganizationHealthRequest(TypedDict, closed=True):
    account_ids: NotRequired["capo_devops_guru.types.account_id_list.AccountIdList"]
    """<p>The ID of the Amazon Web Services account.</p>"""
    organizational_unit_ids: NotRequired[
        "capo_devops_guru.types.organizational_unit_id_list.OrganizationalUnitIdList"
    ]
    """<p>The ID of the organizational unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationHealthRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_devops_guru.types.account_id_list

        out["AccountIds"] = capo_devops_guru.types.account_id_list.serialize_json(
            value["account_ids"]
        )
    if "organizational_unit_ids" in value:
        import capo_devops_guru.types.organizational_unit_id_list

        out["OrganizationalUnitIds"] = (
            capo_devops_guru.types.organizational_unit_id_list.serialize_json(
                value["organizational_unit_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeOrganizationHealthRequest:
    out: DescribeOrganizationHealthRequest = {}  # type: ignore[typeddict-item]
    if "AccountIds" in data:
        import capo_devops_guru.types.account_id_list

        out["account_ids"] = capo_devops_guru.types.account_id_list.deserialize_json(
            data["AccountIds"]
        )
    if "OrganizationalUnitIds" in data:
        import capo_devops_guru.types.organizational_unit_id_list

        out["organizational_unit_ids"] = (
            capo_devops_guru.types.organizational_unit_id_list.deserialize_json(
                data["OrganizationalUnitIds"]
            )
        )
    return out
