"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetObjectTypeAttributeStatisticsStats``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.double
    import capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles


class GetObjectTypeAttributeStatisticsStats(TypedDict, closed=True):
    maximum: "capo_customer_profiles.types.double.Double"
    """<p>The maximum value found in the attribute dataset.</p>"""
    minimum: "capo_customer_profiles.types.double.Double"
    """<p>The minimum value found in the attribute dataset.</p>"""
    average: "capo_customer_profiles.types.double.Double"
    """<p>The arithmetic mean of the attribute values.</p>"""
    standard_deviation: "capo_customer_profiles.types.double.Double"
    """<p>The standard deviation of the attribute values, measuring their spread around the mean.</p>"""
    percentiles: "capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles.GetObjectTypeAttributeStatisticsPercentiles"
    """<p>Percentile distribution statistics for the attribute values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectTypeAttributeStatisticsStats) -> dict:
    out: dict = {}
    out["Maximum"] = value["maximum"]
    out["Minimum"] = value["minimum"]
    out["Average"] = value["average"]
    out["StandardDeviation"] = value["standard_deviation"]
    import capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles

    out["Percentiles"] = (
        capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles.serialize_json(
            value["percentiles"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetObjectTypeAttributeStatisticsStats:
    out: GetObjectTypeAttributeStatisticsStats = {}  # type: ignore[typeddict-item]
    if "Maximum" in data:
        out["maximum"] = data["Maximum"]
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsStats.maximum required"
        )
    if "Minimum" in data:
        out["minimum"] = data["Minimum"]
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsStats.minimum required"
        )
    if "Average" in data:
        out["average"] = data["Average"]
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsStats.average required"
        )
    if "StandardDeviation" in data:
        out["standard_deviation"] = data["StandardDeviation"]
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsStats.standard_deviation required"
        )
    if "Percentiles" in data:
        import capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles

        out["percentiles"] = (
            capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles.deserialize_json(
                data["Percentiles"]
            )
        )
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsStats.percentiles required"
        )
    return out
