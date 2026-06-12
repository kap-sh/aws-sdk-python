"""Generated from Smithy shape ``com.amazonaws.fsx#CreateSvmActiveDirectoryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.net_bios_alias
    import aws_sdk_fsx.types.self_managed_active_directory_configuration


class CreateSvmActiveDirectoryConfiguration(TypedDict):
    net_bios_name: NotRequired["aws_sdk_fsx.types.net_bios_alias.NetBiosAlias"]
    """<p>The NetBIOS name of the Active Directory computer object that will be created for your SVM.</p>"""
    self_managed_active_directory_configuration: NotRequired[
        "aws_sdk_fsx.types.self_managed_active_directory_configuration.SelfManagedActiveDirectoryConfiguration"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSvmActiveDirectoryConfiguration) -> dict:
    out: dict = {}
    if "net_bios_name" in value:
        out["NetBiosName"] = value["net_bios_name"]
    if "self_managed_active_directory_configuration" in value:
        import aws_sdk_fsx.types.self_managed_active_directory_configuration

        out["SelfManagedActiveDirectoryConfiguration"] = (
            aws_sdk_fsx.types.self_managed_active_directory_configuration.serialize_aws_json_1_1(
                value["self_managed_active_directory_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSvmActiveDirectoryConfiguration:
    out: CreateSvmActiveDirectoryConfiguration = {}  # type: ignore[typeddict-item]
    if "NetBiosName" in data:
        out["net_bios_name"] = data["NetBiosName"]
    if "SelfManagedActiveDirectoryConfiguration" in data:
        import aws_sdk_fsx.types.self_managed_active_directory_configuration

        out["self_managed_active_directory_configuration"] = (
            aws_sdk_fsx.types.self_managed_active_directory_configuration.deserialize_aws_json_1_1(
                data["SelfManagedActiveDirectoryConfiguration"]
            )
        )
    return out
