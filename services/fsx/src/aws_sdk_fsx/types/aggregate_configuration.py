"""Generated from Smithy shape ``com.amazonaws.fsx#AggregateConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.aggregates
    import aws_sdk_fsx.types.total_constituents


class AggregateConfiguration(TypedDict):
    aggregates: NotRequired["aws_sdk_fsx.types.aggregates.Aggregates"]
    """<p>The list of aggregates that this volume resides on. Aggregates are storage pools which make up your primary storage tier. Each high-availability (HA) pair has one aggregate. The names of the aggregates map to the names of the aggregates in the ONTAP CLI and REST API. For FlexVols, there will always be a single entry.</p> <p>Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:</p> <ul> <li> <p>The strings in the value of <code>Aggregates</code> are not are not formatted as <code>aggrX</code>, where X is a number between 1 and 12.</p> </li> <li> <p>The value of <code>Aggregates</code> contains aggregates that are not present.</p> </li> <li> <p>One or more of the aggregates supplied are too close to the volume limit to support adding more volumes.</p> </li> </ul>"""
    total_constituents: NotRequired[
        "aws_sdk_fsx.types.total_constituents.TotalConstituents"
    ]
    """<p>The total number of constituents this FlexGroup volume has. Not applicable for FlexVols.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateConfiguration) -> dict:
    out: dict = {}
    if "aggregates" in value:
        import aws_sdk_fsx.types.aggregates

        out["Aggregates"] = aws_sdk_fsx.types.aggregates.serialize_aws_json_1_1(
            value["aggregates"]
        )
    if "total_constituents" in value:
        out["TotalConstituents"] = value["total_constituents"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateConfiguration:
    out: AggregateConfiguration = {}  # type: ignore[typeddict-item]
    if "Aggregates" in data:
        import aws_sdk_fsx.types.aggregates

        out["aggregates"] = aws_sdk_fsx.types.aggregates.deserialize_aws_json_1_1(
            data["Aggregates"]
        )
    if "TotalConstituents" in data:
        out["total_constituents"] = data["TotalConstituents"]
    return out
