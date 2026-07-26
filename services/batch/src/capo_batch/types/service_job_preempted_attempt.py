"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobPreemptedAttempt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.long
    import capo_batch.types.service_resource_id
    import capo_batch.types.string


class ServiceJobPreemptedAttempt(TypedDict, closed=True):
    service_resource_id: NotRequired[
        "capo_batch.types.service_resource_id.ServiceResourceId"
    ]
    """<p>The service resource identifier associated with the service job attempt.</p>"""
    started_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the service job attempt was started.</p>"""
    stopped_at: NotRequired["capo_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the service job attempt stopped running.</p>"""
    status_reason: NotRequired["capo_batch.types.string.String"]
    """<p>A string that provides additional details for the current status of the service job attempt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobPreemptedAttempt) -> dict:
    out: dict = {}
    if "service_resource_id" in value:
        import capo_batch.types.service_resource_id

        out["serviceResourceId"] = capo_batch.types.service_resource_id.serialize_json(
            value["service_resource_id"]
        )
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "stopped_at" in value:
        out["stoppedAt"] = value["stopped_at"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> ServiceJobPreemptedAttempt:
    out: ServiceJobPreemptedAttempt = {}  # type: ignore[typeddict-item]
    if "serviceResourceId" in data:
        import capo_batch.types.service_resource_id

        out["service_resource_id"] = (
            capo_batch.types.service_resource_id.deserialize_json(
                data["serviceResourceId"]
            )
        )
    if "startedAt" in data:
        out["started_at"] = data["startedAt"]
    if "stoppedAt" in data:
        out["stopped_at"] = data["stoppedAt"]
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
