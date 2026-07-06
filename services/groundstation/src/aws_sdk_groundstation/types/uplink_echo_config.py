"""Generated from Smithy shape ``com.amazonaws.groundstation#UplinkEchoConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.config_arn


class UplinkEchoConfig(TypedDict, closed=True):
    enabled: "bool"
    """<p>Whether or not an uplink <code>Config</code> is enabled.</p>"""
    antenna_uplink_config_arn: "aws_sdk_groundstation.types.config_arn.ConfigArn"
    """<p>ARN of an uplink <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UplinkEchoConfig) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    out["antennaUplinkConfigArn"] = value["antenna_uplink_config_arn"]
    return out


def deserialize_json(data: dict) -> UplinkEchoConfig:
    out: UplinkEchoConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("UplinkEchoConfig.enabled required")
    if "antennaUplinkConfigArn" in data:
        out["antenna_uplink_config_arn"] = data["antennaUplinkConfigArn"]
    else:
        raise DeserializationError(
            "UplinkEchoConfig.antenna_uplink_config_arn required"
        )
    return out
