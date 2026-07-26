"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemEndpoints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.file_system_endpoint


class FileSystemEndpoints(TypedDict, closed=True):
    intercluster: NotRequired["capo_fsx.types.file_system_endpoint.FileSystemEndpoint"]
    """<p>An endpoint for managing your file system by setting up NetApp SnapMirror with other ONTAP systems.</p>"""
    management: NotRequired["capo_fsx.types.file_system_endpoint.FileSystemEndpoint"]
    """<p>An endpoint for managing your file system using the NetApp ONTAP CLI and NetApp ONTAP API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemEndpoints) -> dict:
    out: dict = {}
    if "intercluster" in value:
        import capo_fsx.types.file_system_endpoint

        out["Intercluster"] = (
            capo_fsx.types.file_system_endpoint.serialize_aws_json_1_1(
                value["intercluster"]
            )
        )
    if "management" in value:
        import capo_fsx.types.file_system_endpoint

        out["Management"] = capo_fsx.types.file_system_endpoint.serialize_aws_json_1_1(
            value["management"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemEndpoints:
    out: FileSystemEndpoints = {}  # type: ignore[typeddict-item]
    if "Intercluster" in data:
        import capo_fsx.types.file_system_endpoint

        out["intercluster"] = (
            capo_fsx.types.file_system_endpoint.deserialize_aws_json_1_1(
                data["Intercluster"]
            )
        )
    if "Management" in data:
        import capo_fsx.types.file_system_endpoint

        out["management"] = (
            capo_fsx.types.file_system_endpoint.deserialize_aws_json_1_1(
                data["Management"]
            )
        )
    return out
