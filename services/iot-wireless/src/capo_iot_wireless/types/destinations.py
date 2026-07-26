"""Generated from Smithy shape ``com.amazonaws.iotwireless#Destinations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.destination_arn
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.expression
    import capo_iot_wireless.types.expression_type
    import capo_iot_wireless.types.role_arn


class Destinations(TypedDict, closed=True):
    arn: NotRequired["capo_iot_wireless.types.destination_arn.DestinationArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    name: NotRequired["capo_iot_wireless.types.destination_name.DestinationName"]
    """<p>The name of the resource.</p>"""
    expression_type: NotRequired[
        "capo_iot_wireless.types.expression_type.ExpressionType"
    ]
    """<p>The type of value in <code>Expression</code>.</p>"""
    expression: NotRequired["capo_iot_wireless.types.expression.Expression"]
    """<p>The rule name or topic rule to send messages to.</p>"""
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    """<p>The description of the resource.</p>"""
    role_arn: NotRequired["capo_iot_wireless.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM Role that authorizes the destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destinations) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "expression_type" in value:
        import capo_iot_wireless.types.expression_type

        out["ExpressionType"] = capo_iot_wireless.types.expression_type.serialize_json(
            value["expression_type"]
        )
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> Destinations:
    out: Destinations = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ExpressionType" in data:
        import capo_iot_wireless.types.expression_type

        out["expression_type"] = (
            capo_iot_wireless.types.expression_type.deserialize_json(
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
