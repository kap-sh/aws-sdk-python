"""Generated from Smithy shape ``com.amazonaws.fms#EC2ReplaceRouteTableAssociationAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.action_target
    import aws_sdk_fms.types.length_bounded_string


class EC2ReplaceRouteTableAssociationAction(TypedDict):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the ReplaceRouteTableAssociation action in Amazon EC2.</p>"""
    association_id: "aws_sdk_fms.types.action_target.ActionTarget"
    """<p>Information about the association ID.</p>"""
    route_table_id: "aws_sdk_fms.types.action_target.ActionTarget"
    """<p>Information about the ID of the new route table to associate with the subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2ReplaceRouteTableAssociationAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_fms.types.action_target

    out["AssociationId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
        value["association_id"]
    )
    import aws_sdk_fms.types.action_target

    out["RouteTableId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
        value["route_table_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2ReplaceRouteTableAssociationAction:
    out: EC2ReplaceRouteTableAssociationAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "AssociationId" in data:
        import aws_sdk_fms.types.action_target

        out["association_id"] = (
            aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
                data["AssociationId"]
            )
        )
    else:
        raise DeserializationError(
            "EC2ReplaceRouteTableAssociationAction.association_id required"
        )
    if "RouteTableId" in data:
        import aws_sdk_fms.types.action_target

        out["route_table_id"] = (
            aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
                data["RouteTableId"]
            )
        )
    else:
        raise DeserializationError(
            "EC2ReplaceRouteTableAssociationAction.route_table_id required"
        )
    return out
