"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#InputSwitchConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class InputSwitchConfiguration(TypedDict, closed=True):
    mqcs_input_switching: NotRequired["bool"]
    """<p>When true, AWS Elemental MediaPackage performs input switching based on the MQCS. Default is false. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"""
    preferred_input: NotRequired["int"]
    """<p>For CMAF inputs, indicates which input MediaPackage should prefer when both inputs have equal MQCS scores. Select <code>1</code> to prefer the first ingest endpoint, or <code>2</code> to prefer the second ingest endpoint. If you don't specify a preferred input, MediaPackage uses its default switching behavior when MQCS scores are equal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSwitchConfiguration) -> dict:
    out: dict = {}
    if "mqcs_input_switching" in value:
        out["MQCSInputSwitching"] = value["mqcs_input_switching"]
    if "preferred_input" in value:
        out["PreferredInput"] = value["preferred_input"]
    return out


def deserialize_json(data: dict) -> InputSwitchConfiguration:
    out: InputSwitchConfiguration = {}  # type: ignore[typeddict-item]
    if "MQCSInputSwitching" in data:
        out["mqcs_input_switching"] = data["MQCSInputSwitching"]
    if "PreferredInput" in data:
        out["preferred_input"] = data["PreferredInput"]
    return out
