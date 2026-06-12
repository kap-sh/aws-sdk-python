"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateAliasInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.alias_id_or_arn
    import aws_sdk_gamelift.types.non_blank_and_length_constraint_string
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.routing_strategy


class UpdateAliasInput(TypedDict):
    alias_id: NotRequired["aws_sdk_gamelift.types.alias_id_or_arn.AliasIdOrArn"]
    """<p>A unique identifier for the alias that you want to update. You can use either the alias ID or ARN value.</p>"""
    name: NotRequired[
        "aws_sdk_gamelift.types.non_blank_and_length_constraint_string.NonBlankAndLengthConstraintString"
    ]
    """<p>A descriptive label that is associated with an alias. Alias names do not need to be unique.</p>"""
    description: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A human-readable description of the alias.</p>"""
    routing_strategy: NotRequired[
        "aws_sdk_gamelift.types.routing_strategy.RoutingStrategy"
    ]
    """<p>The routing configuration, including routing type and fleet target, for the alias.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAliasInput) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "routing_strategy" in value:
        import aws_sdk_gamelift.types.routing_strategy

        out["RoutingStrategy"] = (
            aws_sdk_gamelift.types.routing_strategy.serialize_aws_json_1_1(
                value["routing_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAliasInput:
    out: UpdateAliasInput = {}  # type: ignore[typeddict-item]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoutingStrategy" in data:
        import aws_sdk_gamelift.types.routing_strategy

        out["routing_strategy"] = (
            aws_sdk_gamelift.types.routing_strategy.deserialize_aws_json_1_1(
                data["RoutingStrategy"]
            )
        )
    return out
