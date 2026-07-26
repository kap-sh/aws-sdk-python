"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QuerySpatialCoverage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.query_spatial_coverage_max


class QuerySpatialCoverage(TypedDict, closed=True):
    max: NotRequired[
        "capo_timestream_query.types.query_spatial_coverage_max.QuerySpatialCoverageMax"
    ]
    """<p>Provides insights into the spatial coverage of the executed query and the table with the most inefficient spatial pruning.</p> <ul> <li> <p> <code>Value</code> – The maximum ratio of spatial coverage.</p> </li> <li> <p> <code>TableArn</code> – The Amazon Resource Name (ARN) of the table with sub-optimal spatial pruning.</p> </li> <li> <p> <code>PartitionKey</code> – The partition key used for partitioning, which can be a default <code>measure_name</code> or a CDPK.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QuerySpatialCoverage) -> dict:
    out: dict = {}
    if "max" in value:
        import capo_timestream_query.types.query_spatial_coverage_max

        out["Max"] = (
            capo_timestream_query.types.query_spatial_coverage_max.serialize_aws_json_1_0(
                value["max"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> QuerySpatialCoverage:
    out: QuerySpatialCoverage = {}  # type: ignore[typeddict-item]
    if "Max" in data:
        import capo_timestream_query.types.query_spatial_coverage_max

        out["max"] = (
            capo_timestream_query.types.query_spatial_coverage_max.deserialize_aws_json_1_0(
                data["Max"]
            )
        )
    return out
