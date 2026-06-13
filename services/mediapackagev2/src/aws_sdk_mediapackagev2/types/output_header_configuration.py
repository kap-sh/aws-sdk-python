"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#OutputHeaderConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class OutputHeaderConfiguration(TypedDict):
    publish_mqcs: NotRequired["bool"]
    """<p>When true, AWS Elemental MediaPackage includes the MQCS in responses to the CDN. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputHeaderConfiguration) -> dict:
    out: dict = {}
    if "publish_mqcs" in value:
        out["PublishMQCS"] = value["publish_mqcs"]
    return out


def deserialize_json(data: dict) -> OutputHeaderConfiguration:
    out: OutputHeaderConfiguration = {}  # type: ignore[typeddict-item]
    if "PublishMQCS" in data:
        out["publish_mqcs"] = data["PublishMQCS"]
    return out
