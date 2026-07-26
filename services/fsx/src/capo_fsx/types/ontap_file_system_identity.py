"""Generated from Smithy shape ``com.amazonaws.fsx#OntapFileSystemIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.ontap_file_system_user_type
    import capo_fsx.types.ontap_unix_file_system_user
    import capo_fsx.types.ontap_windows_file_system_user


class OntapFileSystemIdentity(TypedDict, closed=True):
    type: NotRequired[
        "capo_fsx.types.ontap_file_system_user_type.OntapFileSystemUserType"
    ]
    """<p>Specifies the FSx for ONTAP user identity type. Valid values are <code>UNIX</code> and <code>WINDOWS</code>.</p>"""
    unix_user: NotRequired[
        "capo_fsx.types.ontap_unix_file_system_user.OntapUnixFileSystemUser"
    ]
    """<p>Specifies the UNIX user identity for file system operations.</p>"""
    windows_user: NotRequired[
        "capo_fsx.types.ontap_windows_file_system_user.OntapWindowsFileSystemUser"
    ]
    """<p>Specifies the Windows user identity for file system operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OntapFileSystemIdentity) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_fsx.types.ontap_file_system_user_type

        out["Type"] = capo_fsx.types.ontap_file_system_user_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "unix_user" in value:
        import capo_fsx.types.ontap_unix_file_system_user

        out["UnixUser"] = (
            capo_fsx.types.ontap_unix_file_system_user.serialize_aws_json_1_1(
                value["unix_user"]
            )
        )
    if "windows_user" in value:
        import capo_fsx.types.ontap_windows_file_system_user

        out["WindowsUser"] = (
            capo_fsx.types.ontap_windows_file_system_user.serialize_aws_json_1_1(
                value["windows_user"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OntapFileSystemIdentity:
    out: OntapFileSystemIdentity = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_fsx.types.ontap_file_system_user_type

        out["type"] = (
            capo_fsx.types.ontap_file_system_user_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "UnixUser" in data:
        import capo_fsx.types.ontap_unix_file_system_user

        out["unix_user"] = (
            capo_fsx.types.ontap_unix_file_system_user.deserialize_aws_json_1_1(
                data["UnixUser"]
            )
        )
    if "WindowsUser" in data:
        import capo_fsx.types.ontap_windows_file_system_user

        out["windows_user"] = (
            capo_fsx.types.ontap_windows_file_system_user.deserialize_aws_json_1_1(
                data["WindowsUser"]
            )
        )
    return out
