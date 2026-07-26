"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.client_request_token
    import capo_fsx.types.file_cache_id
    import capo_fsx.types.update_file_cache_lustre_configuration


class UpdateFileCacheRequest(TypedDict, closed=True):
    file_cache_id: NotRequired["capo_fsx.types.file_cache_id.FileCacheId"]
    """<p>The ID of the cache that you are updating.</p>"""
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    lustre_configuration: NotRequired[
        "capo_fsx.types.update_file_cache_lustre_configuration.UpdateFileCacheLustreConfiguration"
    ]
    """<p>The configuration updates for an Amazon File Cache resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileCacheRequest) -> dict:
    out: dict = {}
    if "file_cache_id" in value:
        out["FileCacheId"] = value["file_cache_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "lustre_configuration" in value:
        import capo_fsx.types.update_file_cache_lustre_configuration

        out["LustreConfiguration"] = (
            capo_fsx.types.update_file_cache_lustre_configuration.serialize_aws_json_1_1(
                value["lustre_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileCacheRequest:
    out: UpdateFileCacheRequest = {}  # type: ignore[typeddict-item]
    if "FileCacheId" in data:
        out["file_cache_id"] = data["FileCacheId"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "LustreConfiguration" in data:
        import capo_fsx.types.update_file_cache_lustre_configuration

        out["lustre_configuration"] = (
            capo_fsx.types.update_file_cache_lustre_configuration.deserialize_aws_json_1_1(
                data["LustreConfiguration"]
            )
        )
    return out
