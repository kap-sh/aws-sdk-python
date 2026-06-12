"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobTimeout``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer


class ServiceJobTimeout(TypedDict):
    attempt_duration_seconds: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The maximum duration in seconds that a service job attempt can run. After this time is reached, Batch terminates the service job attempt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobTimeout) -> dict:
    out: dict = {}
    if "attempt_duration_seconds" in value:
        out["attemptDurationSeconds"] = value["attempt_duration_seconds"]
    return out


def deserialize_json(data: dict) -> ServiceJobTimeout:
    out: ServiceJobTimeout = {}  # type: ignore[typeddict-item]
    if "attemptDurationSeconds" in data:
        out["attempt_duration_seconds"] = data["attemptDurationSeconds"]
    return out
