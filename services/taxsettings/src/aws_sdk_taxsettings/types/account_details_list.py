"""Generated from Smithy shape ``com.amazonaws.taxsettings#AccountDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.account_details

AccountDetailsList: TypeAlias = list["aws_sdk_taxsettings.types.account_details.AccountDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountDetailsList) -> list:
    import aws_sdk_taxsettings.types.account_details
    out: list = []
    for item in value:
        out.append(aws_sdk_taxsettings.types.account_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountDetailsList:
    import aws_sdk_taxsettings.types.account_details
    out: AccountDetailsList = []
    for item in data:
        out.append(aws_sdk_taxsettings.types.account_details.deserialize_json(item))
    return out