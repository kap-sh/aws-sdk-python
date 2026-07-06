"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.expression
    import aws_sdk_iot_wireless.types.expression_type
    import aws_sdk_iot_wireless.types.role_arn


class UpdateDestinationRequest(TypedDict, closed=True):
    name: "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    """<p>The new name of the resource.</p>"""
    expression_type: NotRequired[
        "aws_sdk_iot_wireless.types.expression_type.ExpressionType"
    ]
    """<p>The type of value in <code>Expression</code>.</p>"""
    expression: NotRequired["aws_sdk_iot_wireless.types.expression.Expression"]
    """<p>The new rule name or topic rule to send messages to.</p>"""
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    """<p>A new description of the resource.</p>"""
    role_arn: NotRequired["aws_sdk_iot_wireless.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM Role that authorizes the destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDestinationRequest) -> dict:
    out: dict = {}
    if "expression_type" in value:
        import aws_sdk_iot_wireless.types.expression_type

        out["ExpressionType"] = (
            aws_sdk_iot_wireless.types.expression_type.serialize_json(
                value["expression_type"]
            )
        )
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateDestinationRequest:
    out: UpdateDestinationRequest = {}  # type: ignore[typeddict-item]
    if "ExpressionType" in data:
        import aws_sdk_iot_wireless.types.expression_type

        out["expression_type"] = (
            aws_sdk_iot_wireless.types.expression_type.deserialize_json(
                data["ExpressionType"]
            )
        )
    if "Expression" in data:
        out["expression"] = data["Expression"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
