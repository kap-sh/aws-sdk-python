"""Generated from Smithy shape ``com.amazonaws.fms#EC2CopyRouteTableAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.action_target
    import aws_sdk_fms.types.length_bounded_string


class EC2CopyRouteTableAction(TypedDict):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the copied EC2 route table that is associated with the remediation action.</p>"""
    vpc_id: "aws_sdk_fms.types.action_target.ActionTarget"
    """<p>The VPC ID of the copied EC2 route table that is associated with the remediation action.</p>"""
    route_table_id: "aws_sdk_fms.types.action_target.ActionTarget"
    """<p>The ID of the copied EC2 route table that is associated with the remediation action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2CopyRouteTableAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_fms.types.action_target

    out["VpcId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
        value["vpc_id"]
    )
    import aws_sdk_fms.types.action_target

    out["RouteTableId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
        value["route_table_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2CopyRouteTableAction:
    out: EC2CopyRouteTableAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "VpcId" in data:
        import aws_sdk_fms.types.action_target

        out["vpc_id"] = aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
            data["VpcId"]
        )
    else:
        raise DeserializationError("EC2CopyRouteTableAction.vpc_id required")
    if "RouteTableId" in data:
        import aws_sdk_fms.types.action_target

        out["route_table_id"] = (
            aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
                data["RouteTableId"]
            )
        )
    else:
        raise DeserializationError("EC2CopyRouteTableAction.route_table_id required")
    return out
