"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#TimeoutConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.timeout_in_min


class TimeoutConfig(TypedDict, closed=True):
    max_lifetime_timeout_minutes: NotRequired[
        "aws_sdk_iotsecuretunneling.types.timeout_in_min.TimeoutInMin"
    ]
    """<p>The maximum amount of time (in minutes) a tunnel can remain open. If not specified, maxLifetimeTimeoutMinutes defaults to 720 minutes. Valid values are from 1 minute to 12 hours (720 minutes) </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeoutConfig) -> dict:
    out: dict = {}
    if "max_lifetime_timeout_minutes" in value:
        out["maxLifetimeTimeoutMinutes"] = value["max_lifetime_timeout_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeoutConfig:
    out: TimeoutConfig = {}  # type: ignore[typeddict-item]
    if "maxLifetimeTimeoutMinutes" in data:
        out["max_lifetime_timeout_minutes"] = data["maxLifetimeTimeoutMinutes"]
    return out
