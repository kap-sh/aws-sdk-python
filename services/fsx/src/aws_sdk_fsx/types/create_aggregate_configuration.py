"""Generated from Smithy shape ``com.amazonaws.fsx#CreateAggregateConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.aggregate_list_multiplier
    import aws_sdk_fsx.types.aggregates


class CreateAggregateConfiguration(TypedDict):
    aggregates: NotRequired["aws_sdk_fsx.types.aggregates.Aggregates"]
    """<p>Used to specify the names of aggregates on which the volume will be created.</p>"""
    constituents_per_aggregate: NotRequired[
        "aws_sdk_fsx.types.aggregate_list_multiplier.AggregateListMultiplier"
    ]
    """<p>Used to explicitly set the number of constituents within the FlexGroup per storage aggregate. This field is optional when creating a FlexGroup volume. If unspecified, the default value will be 8. This field cannot be provided when creating a FlexVol volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAggregateConfiguration) -> dict:
    out: dict = {}
    if "aggregates" in value:
        import aws_sdk_fsx.types.aggregates

        out["Aggregates"] = aws_sdk_fsx.types.aggregates.serialize_aws_json_1_1(
            value["aggregates"]
        )
    if "constituents_per_aggregate" in value:
        out["ConstituentsPerAggregate"] = value["constituents_per_aggregate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAggregateConfiguration:
    out: CreateAggregateConfiguration = {}  # type: ignore[typeddict-item]
    if "Aggregates" in data:
        import aws_sdk_fsx.types.aggregates

        out["aggregates"] = aws_sdk_fsx.types.aggregates.deserialize_aws_json_1_1(
            data["Aggregates"]
        )
    if "ConstituentsPerAggregate" in data:
        out["constituents_per_aggregate"] = data["ConstituentsPerAggregate"]
    return out
