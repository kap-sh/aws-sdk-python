"""Generated from Smithy shape ``com.amazonaws.batch#DeleteServiceEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class DeleteServiceEnvironmentRequest(TypedDict, closed=True):
    service_environment: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name or ARN of the service environment to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceEnvironmentRequest) -> dict:
    out: dict = {}
    if "service_environment" in value:
        out["serviceEnvironment"] = value["service_environment"]
    return out


def deserialize_json(data: dict) -> DeleteServiceEnvironmentRequest:
    out: DeleteServiceEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "serviceEnvironment" in data:
        out["service_environment"] = data["serviceEnvironment"]
    return out
