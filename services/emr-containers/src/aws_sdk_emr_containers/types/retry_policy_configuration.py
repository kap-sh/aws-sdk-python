"""Generated from Smithy shape ``com.amazonaws.emrcontainers#RetryPolicyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.java_integer


class RetryPolicyConfiguration(TypedDict):
    max_attempts: "aws_sdk_emr_containers.types.java_integer.JavaInteger"
    """<p>The maximum number of attempts on the job's driver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryPolicyConfiguration) -> dict:
    out: dict = {}
    out["maxAttempts"] = value["max_attempts"]
    return out


def deserialize_json(data: dict) -> RetryPolicyConfiguration:
    out: RetryPolicyConfiguration = {}  # type: ignore[typeddict-item]
    if "maxAttempts" in data:
        out["max_attempts"] = data["maxAttempts"]
    else:
        raise DeserializationError("RetryPolicyConfiguration.max_attempts required")
    return out
