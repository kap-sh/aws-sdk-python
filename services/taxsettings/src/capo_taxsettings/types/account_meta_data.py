"""Generated from Smithy shape ``com.amazonaws.taxsettings#AccountMetaData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.account_name
    import capo_taxsettings.types.address
    import capo_taxsettings.types.address_role_map
    import capo_taxsettings.types.address_role_type
    import capo_taxsettings.types.seller


class AccountMetaData(TypedDict, closed=True):
    account_name: NotRequired["capo_taxsettings.types.account_name.AccountName"]
    """<p> The Amazon Web Services accounts name. </p>"""
    seller: NotRequired["capo_taxsettings.types.seller.Seller"]
    """<p> Seller information associated with the account. </p>"""
    address: NotRequired["capo_taxsettings.types.address.Address"]
    address_type: NotRequired[
        "capo_taxsettings.types.address_role_type.AddressRoleType"
    ]
    """<p> The type of address associated with the legal profile. </p>"""
    address_role_map: NotRequired[
        "capo_taxsettings.types.address_role_map.AddressRoleMap"
    ]
    """<p> Address roles associated with the account containing country code information. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountMetaData) -> dict:
    out: dict = {}
    if "account_name" in value:
        out["accountName"] = value["account_name"]
    if "seller" in value:
        out["seller"] = value["seller"]
    if "address" in value:
        import capo_taxsettings.types.address

        out["address"] = capo_taxsettings.types.address.serialize_json(value["address"])
    if "address_type" in value:
        import capo_taxsettings.types.address_role_type

        out["addressType"] = capo_taxsettings.types.address_role_type.serialize_json(
            value["address_type"]
        )
    if "address_role_map" in value:
        import capo_taxsettings.types.address_role_map

        out["addressRoleMap"] = capo_taxsettings.types.address_role_map.serialize_json(
            value["address_role_map"]
        )
    return out


def deserialize_json(data: dict) -> AccountMetaData:
    out: AccountMetaData = {}  # type: ignore[typeddict-item]
    if "accountName" in data:
        out["account_name"] = data["accountName"]
    if "seller" in data:
        out["seller"] = data["seller"]
    if "address" in data:
        import capo_taxsettings.types.address

        out["address"] = capo_taxsettings.types.address.deserialize_json(
            data["address"]
        )
    if "addressType" in data:
        import capo_taxsettings.types.address_role_type

        out["address_type"] = capo_taxsettings.types.address_role_type.deserialize_json(
            data["addressType"]
        )
    if "addressRoleMap" in data:
        import capo_taxsettings.types.address_role_map

        out["address_role_map"] = (
            capo_taxsettings.types.address_role_map.deserialize_json(
                data["addressRoleMap"]
            )
        )
    return out
