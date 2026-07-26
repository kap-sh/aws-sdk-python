"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RecordingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.s3_location


class RecordingConfig(TypedDict, closed=True):
    enabled: "bool"
    """<p>Indicates whether recording is enabled for the browser. When set to true, browser sessions are recorded.</p>"""
    s3_location: NotRequired[
        "capo_bedrock_agentcore_control.types.s3_location.S3Location"
    ]
    """<p>The Amazon S3 location where browser recordings are stored. This location contains the recorded browser sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordingConfig) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "s3_location" in value:
        import capo_bedrock_agentcore_control.types.s3_location

        out["s3Location"] = (
            capo_bedrock_agentcore_control.types.s3_location.serialize_json(
                value["s3_location"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecordingConfig:
    out: RecordingConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "s3Location" in data:
        import capo_bedrock_agentcore_control.types.s3_location

        out["s3_location"] = (
            capo_bedrock_agentcore_control.types.s3_location.deserialize_json(
                data["s3Location"]
            )
        )
    return out
