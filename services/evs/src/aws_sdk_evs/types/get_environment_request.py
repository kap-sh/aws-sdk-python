"""Generated from Smithy shape ``com.amazonaws.evs#GetEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_evs.types.environment_id


class GetEnvironmentRequest(TypedDict):
    environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentRequest:
    out: GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
