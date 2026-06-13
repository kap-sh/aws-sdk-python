"""Generated from Smithy shape ``com.amazonaws.groundstation#TelemetrySinkConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.telemetry_sink_data
    import aws_sdk_groundstation.types.telemetry_sink_type


class TelemetrySinkConfig(TypedDict):
    telemetry_sink_type: (
        "aws_sdk_groundstation.types.telemetry_sink_type.TelemetrySinkType"
    )
    """<p>The type of telemetry sink.</p>"""
    telemetry_sink_data: (
        "aws_sdk_groundstation.types.telemetry_sink_data.TelemetrySinkData"
    )
    """<p>Information about the telemetry sink specified by the <code>telemetrySinkType</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetrySinkConfig) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.telemetry_sink_type

    out["telemetrySinkType"] = (
        aws_sdk_groundstation.types.telemetry_sink_type.serialize_json(
            value["telemetry_sink_type"]
        )
    )
    import aws_sdk_groundstation.types.telemetry_sink_data

    out["telemetrySinkData"] = (
        aws_sdk_groundstation.types.telemetry_sink_data.serialize_json(
            value["telemetry_sink_data"]
        )
    )
    return out


def deserialize_json(data: dict) -> TelemetrySinkConfig:
    out: TelemetrySinkConfig = {}  # type: ignore[typeddict-item]
    if "telemetrySinkType" in data:
        import aws_sdk_groundstation.types.telemetry_sink_type

        out["telemetry_sink_type"] = (
            aws_sdk_groundstation.types.telemetry_sink_type.deserialize_json(
                data["telemetrySinkType"]
            )
        )
    else:
        raise DeserializationError("TelemetrySinkConfig.telemetry_sink_type required")
    if "telemetrySinkData" in data:
        import aws_sdk_groundstation.types.telemetry_sink_data

        out["telemetry_sink_data"] = (
            aws_sdk_groundstation.types.telemetry_sink_data.deserialize_json(
                data["telemetrySinkData"]
            )
        )
    else:
        raise DeserializationError("TelemetrySinkConfig.telemetry_sink_data required")
    return out
