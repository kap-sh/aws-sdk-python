"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetDestinationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.destination_arn
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.expression
    import aws_sdk_iot_wireless.types.expression_type
    import aws_sdk_iot_wireless.types.role_arn


class GetDestinationResponse(TypedDict):
    arn: NotRequired["aws_sdk_iot_wireless.types.destination_arn.DestinationArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    name: NotRequired["aws_sdk_iot_wireless.types.destination_name.DestinationName"]
    """<p>The name of the resource.</p>"""
    expression: NotRequired["aws_sdk_iot_wireless.types.expression.Expression"]
    """<p>The rule name or topic rule to send messages to.</p>"""
    expression_type: NotRequired[
        "aws_sdk_iot_wireless.types.expression_type.ExpressionType"
    ]
    """<p>The type of value in <code>Expression</code>.</p>"""
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    """<p>The description of the resource.</p>"""
    role_arn: NotRequired["aws_sdk_iot_wireless.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM Role that authorizes the destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDestinationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "expression_type" in value:
        import aws_sdk_iot_wireless.types.expression_type

        out["ExpressionType"] = (
            aws_sdk_iot_wireless.types.expression_type.serialize_json(
                value["expression_type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> GetDestinationResponse:
    out: GetDestinationResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    if "ExpressionType" in data:
        import aws_sdk_iot_wireless.types.expression_type

        out["expression_type"] = (
            aws_sdk_iot_wireless.types.expression_type.deserialize_json(
                data["ExpressionType"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
