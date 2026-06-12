"""Generated from Smithy shape ``com.amazonaws.sfn#TracingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sfn.types.enabled


class TracingConfiguration(TypedDict):
    enabled: "aws_sdk_sfn.types.enabled.Enabled"
    """<p>When set to <code>true</code>, X-Ray tracing is enabled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TracingConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> TracingConfiguration:
    out: TracingConfiguration = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
