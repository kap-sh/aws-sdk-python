"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteFileCacheRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.file_cache_id


class DeleteFileCacheRequest(TypedDict):
    file_cache_id: NotRequired["aws_sdk_fsx.types.file_cache_id.FileCacheId"]
    """<p>The ID of the cache that's being deleted.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileCacheRequest) -> dict:
    out: dict = {}
    if "file_cache_id" in value:
        out["FileCacheId"] = value["file_cache_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileCacheRequest:
    out: DeleteFileCacheRequest = {}  # type: ignore[typeddict-item]
    if "FileCacheId" in data:
        out["file_cache_id"] = data["FileCacheId"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
