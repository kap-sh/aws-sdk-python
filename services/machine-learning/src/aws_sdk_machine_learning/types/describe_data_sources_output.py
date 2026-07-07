"""Generated from Smithy shape ``com.amazonaws.machinelearning#DescribeDataSourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.data_sources
    import aws_sdk_machine_learning.types.string_type


class DescribeDataSourcesOutput(TypedDict, closed=True):
    results: NotRequired["aws_sdk_machine_learning.types.data_sources.DataSources"]
    """<p>A list of <code>DataSource</code> that meet the search criteria. </p>"""
    next_token: NotRequired["aws_sdk_machine_learning.types.string_type.StringType"]
    """<p>An ID of the next page in the paginated results that indicates at least one more page follows.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataSourcesOutput) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_machine_learning.types.data_sources

        out["Results"] = (
            aws_sdk_machine_learning.types.data_sources.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataSourcesOutput:
    out: DescribeDataSourcesOutput = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_machine_learning.types.data_sources

        out["results"] = (
            aws_sdk_machine_learning.types.data_sources.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
