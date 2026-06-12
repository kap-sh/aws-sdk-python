"""Generated from Smithy shape ``com.amazonaws.pinpoint#CustomDeliveryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.list_of__endpoint_types_element


class CustomDeliveryConfiguration(TypedDict):
    delivery_uri: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The destination to send the campaign or treatment to. This value can be one of the following:</p> <ul><li><p>The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment.</p></li> <li><p>The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.</p></li></ul>"""
    endpoint_types: NotRequired[
        "aws_sdk_pinpoint.types.list_of__endpoint_types_element.ListOf__EndpointTypesElement"
    ]
    """<p>The types of endpoints to send the campaign or treatment to. Each valid value maps to a type of channel that you can associate with an endpoint by using the ChannelType property of an endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDeliveryConfiguration) -> dict:
    out: dict = {}
    if "delivery_uri" in value:
        out["DeliveryUri"] = value["delivery_uri"]
    if "endpoint_types" in value:
        import aws_sdk_pinpoint.types.list_of__endpoint_types_element

        out["EndpointTypes"] = (
            aws_sdk_pinpoint.types.list_of__endpoint_types_element.serialize_json(
                value["endpoint_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomDeliveryConfiguration:
    out: CustomDeliveryConfiguration = {}  # type: ignore[typeddict-item]
    if "DeliveryUri" in data:
        out["delivery_uri"] = data["DeliveryUri"]
    if "EndpointTypes" in data:
        import aws_sdk_pinpoint.types.list_of__endpoint_types_element

        out["endpoint_types"] = (
            aws_sdk_pinpoint.types.list_of__endpoint_types_element.deserialize_json(
                data["EndpointTypes"]
            )
        )
    return out
