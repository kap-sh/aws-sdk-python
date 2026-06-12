"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaDeviceMount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.file_system_path
    import aws_sdk_greengrassv2.types.lambda_filesystem_permission
    import aws_sdk_greengrassv2.types.optional_boolean


class LambdaDeviceMount(TypedDict):
    path: "aws_sdk_greengrassv2.types.file_system_path.FileSystemPath"
    """<p>The mount path for the device in the file system.</p>"""
    permission: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_filesystem_permission.LambdaFilesystemPermission"
    ]
    """<p>The permission to access the device: read/only (<code>ro</code>) or read/write (<code>rw</code>).</p> <p>Default: <code>ro</code> </p>"""
    add_group_owner: NotRequired[
        "aws_sdk_greengrassv2.types.optional_boolean.OptionalBoolean"
    ]
    """<p>Whether or not to add the component's system user as an owner of the device.</p> <p>Default: <code>false</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaDeviceMount) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    if "permission" in value:
        import aws_sdk_greengrassv2.types.lambda_filesystem_permission

        out["permission"] = (
            aws_sdk_greengrassv2.types.lambda_filesystem_permission.serialize_json(
                value["permission"]
            )
        )
    if "add_group_owner" in value:
        out["addGroupOwner"] = value["add_group_owner"]
    return out


def deserialize_json(data: dict) -> LambdaDeviceMount:
    out: LambdaDeviceMount = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("LambdaDeviceMount.path required")
    if "permission" in data:
        import aws_sdk_greengrassv2.types.lambda_filesystem_permission

        out["permission"] = (
            aws_sdk_greengrassv2.types.lambda_filesystem_permission.deserialize_json(
                data["permission"]
            )
        )
    if "addGroupOwner" in data:
        out["add_group_owner"] = data["addGroupOwner"]
    return out
