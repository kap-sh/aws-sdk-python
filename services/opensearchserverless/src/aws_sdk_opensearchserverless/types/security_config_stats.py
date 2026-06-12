"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#SecurityConfigStats``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SecurityConfigStats(TypedDict):
    saml_config_count: NotRequired["int"]
    """<p>The number of security configurations in the current account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityConfigStats) -> dict:
    out: dict = {}
    if "saml_config_count" in value:
        out["SamlConfigCount"] = value["saml_config_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SecurityConfigStats:
    out: SecurityConfigStats = {}  # type: ignore[typeddict-item]
    if "SamlConfigCount" in data:
        out["saml_config_count"] = data["SamlConfigCount"]
    return out
