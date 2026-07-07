"""Generated from Smithy shape ``com.amazonaws.synthetics#RetryConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.max_retries


class RetryConfigOutput(TypedDict, closed=True):
    max_retries: NotRequired["aws_sdk_synthetics.types.max_retries.MaxRetries"]
    """<p>The maximum number of retries. The value must be less than or equal to 2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryConfigOutput) -> dict:
    out: dict = {}
    if "max_retries" in value:
        out["MaxRetries"] = value["max_retries"]
    return out


def deserialize_json(data: dict) -> RetryConfigOutput:
    out: RetryConfigOutput = {}  # type: ignore[typeddict-item]
    if "MaxRetries" in data:
        out["max_retries"] = data["MaxRetries"]
    return out
