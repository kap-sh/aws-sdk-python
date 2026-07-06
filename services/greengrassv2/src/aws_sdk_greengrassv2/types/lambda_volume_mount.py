"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaVolumeMount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.file_system_path
    import aws_sdk_greengrassv2.types.lambda_filesystem_permission
    import aws_sdk_greengrassv2.types.optional_boolean


class LambdaVolumeMount(TypedDict, closed=True):
    source_path: "aws_sdk_greengrassv2.types.file_system_path.FileSystemPath"
    """<p>The path to the physical volume in the file system.</p>"""
    destination_path: "aws_sdk_greengrassv2.types.file_system_path.FileSystemPath"
    """<p>The path to the logical volume in the file system.</p>"""
    permission: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_filesystem_permission.LambdaFilesystemPermission"
    ]
    """<p>The permission to access the volume: read/only (<code>ro</code>) or read/write (<code>rw</code>).</p> <p>Default: <code>ro</code> </p>"""
    add_group_owner: NotRequired[
        "aws_sdk_greengrassv2.types.optional_boolean.OptionalBoolean"
    ]
    """<p>Whether or not to add the IoT Greengrass user group as an owner of the volume.</p> <p>Default: <code>false</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaVolumeMount) -> dict:
    out: dict = {}
    out["sourcePath"] = value["source_path"]
    out["destinationPath"] = value["destination_path"]
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


def deserialize_json(data: dict) -> LambdaVolumeMount:
    out: LambdaVolumeMount = {}  # type: ignore[typeddict-item]
    if "sourcePath" in data:
        out["source_path"] = data["sourcePath"]
    else:
        raise DeserializationError("LambdaVolumeMount.source_path required")
    if "destinationPath" in data:
        out["destination_path"] = data["destinationPath"]
    else:
        raise DeserializationError("LambdaVolumeMount.destination_path required")
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
