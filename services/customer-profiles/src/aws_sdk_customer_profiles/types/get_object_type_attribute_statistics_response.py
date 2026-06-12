"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetObjectTypeAttributeStatisticsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.get_object_type_attribute_statistics_stats
    import aws_sdk_customer_profiles.types.timestamp


class GetObjectTypeAttributeStatisticsResponse(TypedDict):
    statistics: "aws_sdk_customer_profiles.types.get_object_type_attribute_statistics_stats.GetObjectTypeAttributeStatisticsStats"
    """<p>The statistics.</p>"""
    calculated_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>Time when this statistics was calculated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectTypeAttributeStatisticsResponse) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.get_object_type_attribute_statistics_stats

    out["Statistics"] = (
        aws_sdk_customer_profiles.types.get_object_type_attribute_statistics_stats.serialize_json(
            value["statistics"]
        )
    )
    import aws_sdk_customer_profiles.types.timestamp

    out["CalculatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["calculated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetObjectTypeAttributeStatisticsResponse:
    out: GetObjectTypeAttributeStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "Statistics" in data:
        import aws_sdk_customer_profiles.types.get_object_type_attribute_statistics_stats

        out["statistics"] = (
            aws_sdk_customer_profiles.types.get_object_type_attribute_statistics_stats.deserialize_json(
                data["Statistics"]
            )
        )
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsResponse.statistics required"
        )
    if "CalculatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["calculated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["CalculatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsResponse.calculated_at required"
        )
    return out
