"""Generated from Smithy shape ``com.amazonaws.amplify#CreateDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.app_id
    import capo_amplify.types.branch_name
    import capo_amplify.types.file_map


class CreateDeploymentRequest(TypedDict, closed=True):
    app_id: "capo_amplify.types.app_id.AppId"
    """<p> The unique ID for an Amplify app. </p>"""
    branch_name: "capo_amplify.types.branch_name.BranchName"
    """<p> The name of the branch to use for the job. </p>"""
    file_map: NotRequired["capo_amplify.types.file_map.FileMap"]
    """<p> An optional file map that contains the file name as the key and the file content md5 hash as the value. If this argument is provided, the service will generate a unique upload URL per file. Otherwise, the service will only generate a single upload URL for the zipped files. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentRequest) -> dict:
    out: dict = {}
    if "file_map" in value:
        import capo_amplify.types.file_map

        out["fileMap"] = capo_amplify.types.file_map.serialize_json(value["file_map"])
    return out


def deserialize_json(data: dict) -> CreateDeploymentRequest:
    out: CreateDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "fileMap" in data:
        import capo_amplify.types.file_map

        out["file_map"] = capo_amplify.types.file_map.deserialize_json(data["fileMap"])
    return out
