"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetObjectTypeAttributeStatisticsPercentiles``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.double


class GetObjectTypeAttributeStatisticsPercentiles(TypedDict, closed=True):
    p5: "capo_customer_profiles.types.double.Double"
    """<p>The 5th percentile value of the attribute.</p>"""
    p25: "capo_customer_profiles.types.double.Double"
    """<p>The 25th percentile value of the attribute.</p>"""
    p50: "capo_customer_profiles.types.double.Double"
    """<p>The 50th percentile (median) value of the attribute.</p>"""
    p75: "capo_customer_profiles.types.double.Double"
    """<p>The 75th percentile value of the attribute.</p>"""
    p95: "capo_customer_profiles.types.double.Double"
    """<p>The 95th percentile value of the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectTypeAttributeStatisticsPercentiles) -> dict:
    out: dict = {}
    out["P5"] = value["p5"]
    out["P25"] = value["p25"]
    out["P50"] = value["p50"]
    out["P75"] = value["p75"]
    out["P95"] = value["p95"]
    return out


def deserialize_json(data: dict) -> GetObjectTypeAttributeStatisticsPercentiles:
    out: GetObjectTypeAttributeStatisticsPercentiles = {}  # type: ignore[typeddict-item]
    if "P5" in data:
        out["p5"] = data["P5"]
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsPercentiles.p5 required"
        )
    if "P25" in data:
        out["p25"] = data["P25"]
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsPercentiles.p25 required"
        )
    if "P50" in data:
        out["p50"] = data["P50"]
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsPercentiles.p50 required"
        )
    if "P75" in data:
        out["p75"] = data["P75"]
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsPercentiles.p75 required"
        )
    if "P95" in data:
        out["p95"] = data["P95"]
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsPercentiles.p95 required"
        )
    return out
