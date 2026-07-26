"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateDataLakeOrganizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list


class CreateDataLakeOrganizationConfigurationRequest(TypedDict, closed=True):
    auto_enable_new_account: NotRequired[
        "capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list.DataLakeAutoEnableNewAccountConfigurationList"
    ]
    """<p>Enable Security Lake with the specified configuration settings, to begin collecting security data for new accounts in your organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataLakeOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    if "auto_enable_new_account" in value:
        import capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list

        out["autoEnableNewAccount"] = (
            capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list.serialize_json(
                value["auto_enable_new_account"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDataLakeOrganizationConfigurationRequest:
    out: CreateDataLakeOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "autoEnableNewAccount" in data:
        import capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list

        out["auto_enable_new_account"] = (
            capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list.deserialize_json(
                data["autoEnableNewAccount"]
            )
        )
    return out
