"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemEndpoints``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_system_endpoint


class FileSystemEndpoints(TypedDict):
    intercluster: NotRequired[
        "aws_sdk_fsx.types.file_system_endpoint.FileSystemEndpoint"
    ]
    """<p>An endpoint for managing your file system by setting up NetApp SnapMirror with other ONTAP systems.</p>"""
    management: NotRequired["aws_sdk_fsx.types.file_system_endpoint.FileSystemEndpoint"]
    """<p>An endpoint for managing your file system using the NetApp ONTAP CLI and NetApp ONTAP API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemEndpoints) -> dict:
    out: dict = {}
    if "intercluster" in value:
        import aws_sdk_fsx.types.file_system_endpoint

        out["Intercluster"] = (
            aws_sdk_fsx.types.file_system_endpoint.serialize_aws_json_1_1(
                value["intercluster"]
            )
        )
    if "management" in value:
        import aws_sdk_fsx.types.file_system_endpoint

        out["Management"] = (
            aws_sdk_fsx.types.file_system_endpoint.serialize_aws_json_1_1(
                value["management"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemEndpoints:
    out: FileSystemEndpoints = {}  # type: ignore[typeddict-item]
    if "Intercluster" in data:
        import aws_sdk_fsx.types.file_system_endpoint

        out["intercluster"] = (
            aws_sdk_fsx.types.file_system_endpoint.deserialize_aws_json_1_1(
                data["Intercluster"]
            )
        )
    if "Management" in data:
        import aws_sdk_fsx.types.file_system_endpoint

        out["management"] = (
            aws_sdk_fsx.types.file_system_endpoint.deserialize_aws_json_1_1(
                data["Management"]
            )
        )
    return out
