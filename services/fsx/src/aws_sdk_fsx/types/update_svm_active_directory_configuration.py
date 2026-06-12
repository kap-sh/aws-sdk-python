"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateSvmActiveDirectoryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.net_bios_alias
    import aws_sdk_fsx.types.self_managed_active_directory_configuration_updates


class UpdateSvmActiveDirectoryConfiguration(TypedDict):
    self_managed_active_directory_configuration: NotRequired[
        "aws_sdk_fsx.types.self_managed_active_directory_configuration_updates.SelfManagedActiveDirectoryConfigurationUpdates"
    ]
    net_bios_name: NotRequired["aws_sdk_fsx.types.net_bios_alias.NetBiosAlias"]
    """<p>Specifies an updated NetBIOS name of the AD computer object <code>NetBiosName</code> to which an SVM is joined.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSvmActiveDirectoryConfiguration) -> dict:
    out: dict = {}
    if "self_managed_active_directory_configuration" in value:
        import aws_sdk_fsx.types.self_managed_active_directory_configuration_updates

        out["SelfManagedActiveDirectoryConfiguration"] = (
            aws_sdk_fsx.types.self_managed_active_directory_configuration_updates.serialize_aws_json_1_1(
                value["self_managed_active_directory_configuration"]
            )
        )
    if "net_bios_name" in value:
        out["NetBiosName"] = value["net_bios_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSvmActiveDirectoryConfiguration:
    out: UpdateSvmActiveDirectoryConfiguration = {}  # type: ignore[typeddict-item]
    if "SelfManagedActiveDirectoryConfiguration" in data:
        import aws_sdk_fsx.types.self_managed_active_directory_configuration_updates

        out["self_managed_active_directory_configuration"] = (
            aws_sdk_fsx.types.self_managed_active_directory_configuration_updates.deserialize_aws_json_1_1(
                data["SelfManagedActiveDirectoryConfiguration"]
            )
        )
    if "NetBiosName" in data:
        out["net_bios_name"] = data["NetBiosName"]
    return out
