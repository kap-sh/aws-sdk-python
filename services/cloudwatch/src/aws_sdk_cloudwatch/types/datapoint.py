"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Datapoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.datapoint_value
    import aws_sdk_cloudwatch.types.datapoint_value_map
    import aws_sdk_cloudwatch.types.standard_unit
    import aws_sdk_cloudwatch.types.timestamp


class Datapoint(TypedDict, closed=True):
    timestamp: NotRequired["aws_sdk_cloudwatch.types.timestamp.Timestamp"]
    """<p>The time stamp used for the data point.</p>"""
    sample_count: NotRequired["aws_sdk_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The number of metric values that contributed to the aggregate value of this data point.</p>"""
    average: NotRequired["aws_sdk_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The average of the metric values that correspond to the data point.</p>"""
    sum: NotRequired["aws_sdk_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The sum of the metric values for the data point.</p>"""
    minimum: NotRequired["aws_sdk_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The minimum metric value for the data point.</p>"""
    maximum: NotRequired["aws_sdk_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The maximum metric value for the data point.</p>"""
    unit: NotRequired["aws_sdk_cloudwatch.types.standard_unit.StandardUnit"]
    """<p>The standard unit for the data point.</p>"""
    extended_statistics: NotRequired[
        "aws_sdk_cloudwatch.types.datapoint_value_map.DatapointValueMap"
    ]
    """<p>The percentile statistic for the data point.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Datapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_cloudwatch.types.timestamp

        out["Timestamp"] = aws_sdk_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["timestamp"]
        )
    if "sample_count" in value:
        out["SampleCount"] = value["sample_count"]
    if "average" in value:
        out["Average"] = value["average"]
    if "sum" in value:
        out["Sum"] = value["sum"]
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    if "unit" in value:
        import aws_sdk_cloudwatch.types.standard_unit

        out["Unit"] = aws_sdk_cloudwatch.types.standard_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    if "extended_statistics" in value:
        import aws_sdk_cloudwatch.types.datapoint_value_map

        out["ExtendedStatistics"] = (
            aws_sdk_cloudwatch.types.datapoint_value_map.serialize_aws_json_1_0(
                value["extended_statistics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Datapoint:
    out: Datapoint = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_cloudwatch.types.timestamp

        out["timestamp"] = aws_sdk_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["Timestamp"]
        )
    if "SampleCount" in data:
        out["sample_count"] = data["SampleCount"]
    if "Average" in data:
        out["average"] = data["Average"]
    if "Sum" in data:
        out["sum"] = data["Sum"]
    if "Minimum" in data:
        out["minimum"] = data["Minimum"]
    if "Maximum" in data:
        out["maximum"] = data["Maximum"]
    if "Unit" in data:
        import aws_sdk_cloudwatch.types.standard_unit

        out["unit"] = aws_sdk_cloudwatch.types.standard_unit.deserialize_aws_json_1_0(
            data["Unit"]
        )
    if "ExtendedStatistics" in data:
        import aws_sdk_cloudwatch.types.datapoint_value_map

        out["extended_statistics"] = (
            aws_sdk_cloudwatch.types.datapoint_value_map.deserialize_aws_json_1_0(
                data["ExtendedStatistics"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: Datapoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "timestamp" in value:
        import aws_sdk_cloudwatch.types.timestamp

        aws_sdk_cloudwatch.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{prefix}.Timestamp"
        )
    if "sample_count" in value:
        pairs.append((f"{prefix}.SampleCount", str(value["sample_count"])))
    if "average" in value:
        pairs.append((f"{prefix}.Average", str(value["average"])))
    if "sum" in value:
        pairs.append((f"{prefix}.Sum", str(value["sum"])))
    if "minimum" in value:
        pairs.append((f"{prefix}.Minimum", str(value["minimum"])))
    if "maximum" in value:
        pairs.append((f"{prefix}.Maximum", str(value["maximum"])))
    if "unit" in value:
        import aws_sdk_cloudwatch.types.standard_unit

        aws_sdk_cloudwatch.types.standard_unit.serialize_query(
            value["unit"], pairs, f"{prefix}.Unit"
        )
    if "extended_statistics" in value:
        import aws_sdk_cloudwatch.types.datapoint_value_map

        aws_sdk_cloudwatch.types.datapoint_value_map.serialize_query(
            value["extended_statistics"], pairs, f"{prefix}.ExtendedStatistics"
        )


def deserialize_query(el: Element) -> Datapoint:
    out: Datapoint = {}  # type: ignore[typeddict-item]
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import aws_sdk_cloudwatch.types.timestamp

        out["timestamp"] = aws_sdk_cloudwatch.types.timestamp.deserialize_query(
            child_timestamp
        )
    child_sample_count = el.find("SampleCount")
    if child_sample_count is not None:
        out["sample_count"] = float(child_sample_count.text or "")
    child_average = el.find("Average")
    if child_average is not None:
        out["average"] = float(child_average.text or "")
    child_sum = el.find("Sum")
    if child_sum is not None:
        out["sum"] = float(child_sum.text or "")
    child_minimum = el.find("Minimum")
    if child_minimum is not None:
        out["minimum"] = float(child_minimum.text or "")
    child_maximum = el.find("Maximum")
    if child_maximum is not None:
        out["maximum"] = float(child_maximum.text or "")
    child_unit = el.find("Unit")
    if child_unit is not None:
        import aws_sdk_cloudwatch.types.standard_unit

        out["unit"] = aws_sdk_cloudwatch.types.standard_unit.deserialize_query(
            child_unit
        )
    child_extended_statistics = el.find("ExtendedStatistics")
    if child_extended_statistics is not None:
        import aws_sdk_cloudwatch.types.datapoint_value_map

        out["extended_statistics"] = (
            aws_sdk_cloudwatch.types.datapoint_value_map.deserialize_query(
                child_extended_statistics
            )
        )
    return out
