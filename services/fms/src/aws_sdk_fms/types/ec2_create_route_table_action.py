"""Generated from Smithy shape ``com.amazonaws.fms#EC2CreateRouteTableAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.action_target
    import aws_sdk_fms.types.length_bounded_string


class EC2CreateRouteTableAction(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the CreateRouteTable action.</p>"""
    vpc_id: "aws_sdk_fms.types.action_target.ActionTarget"
    """<p>Information about the ID of a VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2CreateRouteTableAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_fms.types.action_target

    out["VpcId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
        value["vpc_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2CreateRouteTableAction:
    out: EC2CreateRouteTableAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "VpcId" in data:
        import aws_sdk_fms.types.action_target

        out["vpc_id"] = aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
            data["VpcId"]
        )
    else:
        raise DeserializationError("EC2CreateRouteTableAction.vpc_id required")
    return out
