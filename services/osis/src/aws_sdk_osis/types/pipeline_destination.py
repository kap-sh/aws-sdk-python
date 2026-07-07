"""Generated from Smithy shape ``com.amazonaws.osis#PipelineDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.string


class PipelineDestination(TypedDict, closed=True):
    service_name: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>The name of the service receiving data from the pipeline.</p>"""
    endpoint: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>The endpoint receiving data from the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineDestination) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    return out


def deserialize_json(data: dict) -> PipelineDestination:
    out: PipelineDestination = {}  # type: ignore[typeddict-item]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    return out
