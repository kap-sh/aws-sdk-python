"""Generated from Smithy shape ``com.amazonaws.resiliencehub#StartMetricsExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.client_token
    import aws_sdk_resiliencehub.types.entity_name


class StartMetricsExportRequest(TypedDict, closed=True):
    bucket_name: NotRequired["aws_sdk_resiliencehub.types.entity_name.EntityName"]
    """<p>(Optional) Specifies the name of the Amazon Simple Storage Service bucket where the exported metrics will be stored.</p>"""
    client_token: NotRequired["aws_sdk_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMetricsExportRequest) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartMetricsExportRequest:
    out: StartMetricsExportRequest = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
