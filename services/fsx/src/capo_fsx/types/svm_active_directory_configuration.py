"""Generated from Smithy shape ``com.amazonaws.fsx#SvmActiveDirectoryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.net_bios_alias
    import capo_fsx.types.self_managed_active_directory_attributes


class SvmActiveDirectoryConfiguration(TypedDict, closed=True):
    net_bios_name: NotRequired["capo_fsx.types.net_bios_alias.NetBiosAlias"]
    """<p>The NetBIOS name of the AD computer object to which the SVM is joined.</p>"""
    self_managed_active_directory_configuration: NotRequired[
        "capo_fsx.types.self_managed_active_directory_attributes.SelfManagedActiveDirectoryAttributes"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SvmActiveDirectoryConfiguration) -> dict:
    out: dict = {}
    if "net_bios_name" in value:
        out["NetBiosName"] = value["net_bios_name"]
    if "self_managed_active_directory_configuration" in value:
        import capo_fsx.types.self_managed_active_directory_attributes

        out["SelfManagedActiveDirectoryConfiguration"] = (
            capo_fsx.types.self_managed_active_directory_attributes.serialize_aws_json_1_1(
                value["self_managed_active_directory_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SvmActiveDirectoryConfiguration:
    out: SvmActiveDirectoryConfiguration = {}  # type: ignore[typeddict-item]
    if "NetBiosName" in data:
        out["net_bios_name"] = data["NetBiosName"]
    if "SelfManagedActiveDirectoryConfiguration" in data:
        import capo_fsx.types.self_managed_active_directory_attributes

        out["self_managed_active_directory_configuration"] = (
            capo_fsx.types.self_managed_active_directory_attributes.deserialize_aws_json_1_1(
                data["SelfManagedActiveDirectoryConfiguration"]
            )
        )
    return out
