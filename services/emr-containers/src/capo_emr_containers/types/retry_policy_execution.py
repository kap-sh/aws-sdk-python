"""Generated from Smithy shape ``com.amazonaws.emrcontainers#RetryPolicyExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.java_integer


class RetryPolicyExecution(TypedDict, closed=True):
    current_attempt_count: "capo_emr_containers.types.java_integer.JavaInteger"
    """<p>The current number of attempts made on the driver of the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryPolicyExecution) -> dict:
    out: dict = {}
    out["currentAttemptCount"] = value["current_attempt_count"]
    return out


def deserialize_json(data: dict) -> RetryPolicyExecution:
    out: RetryPolicyExecution = {}  # type: ignore[typeddict-item]
    if "currentAttemptCount" in data:
        out["current_attempt_count"] = data["currentAttemptCount"]
    else:
        raise DeserializationError(
            "RetryPolicyExecution.current_attempt_count required"
        )
    return out
