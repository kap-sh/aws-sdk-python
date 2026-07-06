"""Generated from Smithy shape ``com.amazonaws.securitylake#DeleteDataLakeOrganizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration_list


class DeleteDataLakeOrganizationConfigurationRequest(TypedDict, closed=True):
    auto_enable_new_account: NotRequired[
        "aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration_list.DataLakeAutoEnableNewAccountConfigurationList"
    ]
    """<p>Turns off automatic enablement of Security Lake for member accounts that are added to an organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataLakeOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    if "auto_enable_new_account" in value:
        import aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration_list

        out["autoEnableNewAccount"] = (
            aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration_list.serialize_json(
                value["auto_enable_new_account"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteDataLakeOrganizationConfigurationRequest:
    out: DeleteDataLakeOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "autoEnableNewAccount" in data:
        import aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration_list

        out["auto_enable_new_account"] = (
            aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration_list.deserialize_json(
                data["autoEnableNewAccount"]
            )
        )
    return out
