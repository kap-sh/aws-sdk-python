"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EnclaveOptionsRequest``."""

from typing_extensions import NotRequired, TypedDict


class EnclaveOptionsRequest(TypedDict, closed=True):
    enabled: NotRequired["bool"]
    """<p>Enables or disables AWS Nitro Enclaves for enhanced security.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnclaveOptionsRequest) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EnclaveOptionsRequest:
    out: EnclaveOptionsRequest = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
