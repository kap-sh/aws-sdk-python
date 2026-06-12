"""Generated from Smithy shape ``com.amazonaws.fms#EC2AssociateRouteTableAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.action_target
    import aws_sdk_fms.types.length_bounded_string


class EC2AssociateRouteTableAction(TypedDict):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the EC2 route table that is associated with the remediation action.</p>"""
    route_table_id: "aws_sdk_fms.types.action_target.ActionTarget"
    """<p>The ID of the EC2 route table that is associated with the remediation action.</p>"""
    subnet_id: NotRequired["aws_sdk_fms.types.action_target.ActionTarget"]
    """<p>The ID of the subnet for the EC2 route table that is associated with the remediation action.</p>"""
    gateway_id: NotRequired["aws_sdk_fms.types.action_target.ActionTarget"]
    """<p>The ID of the gateway to be used with the EC2 route table that is associated with the remediation action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2AssociateRouteTableAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_fms.types.action_target

    out["RouteTableId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
        value["route_table_id"]
    )
    if "subnet_id" in value:
        import aws_sdk_fms.types.action_target

        out["SubnetId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
            value["subnet_id"]
        )
    if "gateway_id" in value:
        import aws_sdk_fms.types.action_target

        out["GatewayId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
            value["gateway_id"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2AssociateRouteTableAction:
    out: EC2AssociateRouteTableAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RouteTableId" in data:
        import aws_sdk_fms.types.action_target

        out["route_table_id"] = (
            aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
                data["RouteTableId"]
            )
        )
    else:
        raise DeserializationError(
            "EC2AssociateRouteTableAction.route_table_id required"
        )
    if "SubnetId" in data:
        import aws_sdk_fms.types.action_target

        out["subnet_id"] = aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
            data["SubnetId"]
        )
    if "GatewayId" in data:
        import aws_sdk_fms.types.action_target

        out["gateway_id"] = aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
            data["GatewayId"]
        )
    return out
