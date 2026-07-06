"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.delivery_destination_arn
    import aws_sdk_iot_managed_integrations.types.delivery_destination_role_arn
    import aws_sdk_iot_managed_integrations.types.delivery_destination_type
    import aws_sdk_iot_managed_integrations.types.destination_description
    import aws_sdk_iot_managed_integrations.types.destination_name


class UpdateDestinationRequest(TypedDict, closed=True):
    name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName"
    """<p>The name of the customer-managed destination.</p>"""
    delivery_destination_arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>"""
    delivery_destination_type: NotRequired[
        "aws_sdk_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType"
    ]
    """<p>The destination type for the customer-managed destination.</p>"""
    role_arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the delivery destination role.</p>"""
    description: NotRequired[
        "aws_sdk_iot_managed_integrations.types.destination_description.DestinationDescription"
    ]
    """<p>The description of the customer-managed destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDestinationRequest) -> dict:
    out: dict = {}
    if "delivery_destination_arn" in value:
        out["DeliveryDestinationArn"] = value["delivery_destination_arn"]
    if "delivery_destination_type" in value:
        import aws_sdk_iot_managed_integrations.types.delivery_destination_type

        out["DeliveryDestinationType"] = (
            aws_sdk_iot_managed_integrations.types.delivery_destination_type.serialize_json(
                value["delivery_destination_type"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateDestinationRequest:
    out: UpdateDestinationRequest = {}  # type: ignore[typeddict-item]
    if "DeliveryDestinationArn" in data:
        out["delivery_destination_arn"] = data["DeliveryDestinationArn"]
    if "DeliveryDestinationType" in data:
        import aws_sdk_iot_managed_integrations.types.delivery_destination_type

        out["delivery_destination_type"] = (
            aws_sdk_iot_managed_integrations.types.delivery_destination_type.deserialize_json(
                data["DeliveryDestinationType"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
