"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservedCapacityDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.dynamo_db_capacity_details


class ReservedCapacityDetails(TypedDict):
    dynamo_db_capacity_details: NotRequired[
        "aws_sdk_cost_explorer.types.dynamo_db_capacity_details.DynamoDBCapacityDetails"
    ]
    """<p>The DynamoDB reservations that Amazon Web Services recommends that you purchase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedCapacityDetails) -> dict:
    out: dict = {}
    if "dynamo_db_capacity_details" in value:
        import aws_sdk_cost_explorer.types.dynamo_db_capacity_details

        out["DynamoDBCapacityDetails"] = (
            aws_sdk_cost_explorer.types.dynamo_db_capacity_details.serialize_aws_json_1_1(
                value["dynamo_db_capacity_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservedCapacityDetails:
    out: ReservedCapacityDetails = {}  # type: ignore[typeddict-item]
    if "DynamoDBCapacityDetails" in data:
        import aws_sdk_cost_explorer.types.dynamo_db_capacity_details

        out["dynamo_db_capacity_details"] = (
            aws_sdk_cost_explorer.types.dynamo_db_capacity_details.deserialize_aws_json_1_1(
                data["DynamoDBCapacityDetails"]
            )
        )
    return out
