"""Generated from Smithy shape ``com.amazonaws.batch#LatestServiceJobAttempt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.service_resource_id


class LatestServiceJobAttempt(TypedDict, closed=True):
    service_resource_id: NotRequired[
        "capo_batch.types.service_resource_id.ServiceResourceId"
    ]
    """<p>The service resource identifier associated with the service job attempt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LatestServiceJobAttempt) -> dict:
    out: dict = {}
    if "service_resource_id" in value:
        import capo_batch.types.service_resource_id

        out["serviceResourceId"] = capo_batch.types.service_resource_id.serialize_json(
            value["service_resource_id"]
        )
    return out


def deserialize_json(data: dict) -> LatestServiceJobAttempt:
    out: LatestServiceJobAttempt = {}  # type: ignore[typeddict-item]
    if "serviceResourceId" in data:
        import capo_batch.types.service_resource_id

        out["service_resource_id"] = (
            capo_batch.types.service_resource_id.deserialize_json(
                data["serviceResourceId"]
            )
        )
    return out
