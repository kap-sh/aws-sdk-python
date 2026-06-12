"""Generated from Smithy shape ``com.amazonaws.xray#SamplingBoost``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.double
    import aws_sdk_xray.types.timestamp


class SamplingBoost(TypedDict):
    boost_rate: "aws_sdk_xray.types.double.Double"
    """<p>The calculated sampling boost rate for this service </p>"""
    boost_rate_ttl: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p>When the sampling boost expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingBoost) -> dict:
    out: dict = {}
    out["BoostRate"] = value.get("boost_rate", 0)
    import aws_sdk_xray.types.timestamp

    out["BoostRateTTL"] = aws_sdk_xray.types.timestamp.serialize_json(
        value["boost_rate_ttl"]
    )
    return out


def deserialize_json(data: dict) -> SamplingBoost:
    out: SamplingBoost = {}  # type: ignore[typeddict-item]
    if "BoostRate" in data:
        out["boost_rate"] = data["BoostRate"]
    else:
        out["boost_rate"] = 0
    if "BoostRateTTL" in data:
        import aws_sdk_xray.types.timestamp

        out["boost_rate_ttl"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["BoostRateTTL"]
        )
    else:
        raise DeserializationError("SamplingBoost.boost_rate_ttl required")
    return out
