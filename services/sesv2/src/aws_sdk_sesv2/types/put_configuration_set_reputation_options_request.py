"""Generated from Smithy shape ``com.amazonaws.sesv2#PutConfigurationSetReputationOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.configuration_set_name
    import aws_sdk_sesv2.types.enabled


class PutConfigurationSetReputationOptionsRequest(TypedDict):
    configuration_set_name: (
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set.</p>"""
    reputation_metrics_enabled: "aws_sdk_sesv2.types.enabled.Enabled"
    """<p>If <code>true</code>, tracking of reputation metrics is enabled for the configuration set. If <code>false</code>, tracking of reputation metrics is disabled for the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetReputationOptionsRequest) -> dict:
    out: dict = {}
    out["ReputationMetricsEnabled"] = value.get("reputation_metrics_enabled", False)
    return out


def deserialize_json(data: dict) -> PutConfigurationSetReputationOptionsRequest:
    out: PutConfigurationSetReputationOptionsRequest = {}  # type: ignore[typeddict-item]
    if "ReputationMetricsEnabled" in data:
        out["reputation_metrics_enabled"] = data["ReputationMetricsEnabled"]
    else:
        out["reputation_metrics_enabled"] = False
    return out
