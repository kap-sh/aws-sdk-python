"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImportVmImageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.image_logging_configuration
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.os_version
    import aws_sdk_imagebuilder.types.platform
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.version_number


class ImportVmImageRequest(TypedDict):
    name: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The name of the base image that is created by the import process.</p>"""
    semantic_version: "aws_sdk_imagebuilder.types.version_number.VersionNumber"
    """<p>The semantic version to attach to the base image that was created during the import process. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description for the base image that is created by the import process.</p>"""
    platform: "aws_sdk_imagebuilder.types.platform.Platform"
    """<p>The operating system platform for the imported VM.</p>"""
    os_version: NotRequired["aws_sdk_imagebuilder.types.os_version.OsVersion"]
    """<p>The operating system version for the imported VM.</p>"""
    vm_import_task_id: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The <code>importTaskId</code> (API) or <code>ImportTaskId</code> (CLI) from the Amazon EC2 VM import process. Image Builder retrieves information from the import process to pull in the AMI that is created from the VM source as the base image for your recipe.</p>"""
    logging_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
    ]
    """<p>Define logging configuration for the image build process.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are attached to the import resources.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportVmImageRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["semanticVersion"] = value["semantic_version"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_imagebuilder.types.platform

    out["platform"] = aws_sdk_imagebuilder.types.platform.serialize_json(
        value["platform"]
    )
    if "os_version" in value:
        out["osVersion"] = value["os_version"]
    out["vmImportTaskId"] = value["vm_import_task_id"]
    if "logging_configuration" in value:
        import aws_sdk_imagebuilder.types.image_logging_configuration

        out["loggingConfiguration"] = (
            aws_sdk_imagebuilder.types.image_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportVmImageRequest:
    out: ImportVmImageRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ImportVmImageRequest.name required")
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("ImportVmImageRequest.semantic_version required")
    if "description" in data:
        out["description"] = data["description"]
    if "platform" in data:
        import aws_sdk_imagebuilder.types.platform

        out["platform"] = aws_sdk_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    else:
        raise DeserializationError("ImportVmImageRequest.platform required")
    if "osVersion" in data:
        out["os_version"] = data["osVersion"]
    if "vmImportTaskId" in data:
        out["vm_import_task_id"] = data["vmImportTaskId"]
    else:
        raise DeserializationError("ImportVmImageRequest.vm_import_task_id required")
    if "loggingConfiguration" in data:
        import aws_sdk_imagebuilder.types.image_logging_configuration

        out["logging_configuration"] = (
            aws_sdk_imagebuilder.types.image_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("ImportVmImageRequest.client_token required")
    return out
