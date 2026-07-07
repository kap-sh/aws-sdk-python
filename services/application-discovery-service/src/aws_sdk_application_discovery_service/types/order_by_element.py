"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#OrderByElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.order_by_element_field_name
    import aws_sdk_application_discovery_service.types.order_string


class OrderByElement(TypedDict, closed=True):
    field_name: "aws_sdk_application_discovery_service.types.order_by_element_field_name.OrderByElementFieldName"
    """<p>The field on which to order.</p>"""
    sort_order: NotRequired[
        "aws_sdk_application_discovery_service.types.order_string.orderString"
    ]
    """<p>Ordering direction.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrderByElement) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    if "sort_order" in value:
        import aws_sdk_application_discovery_service.types.order_string

        out["sortOrder"] = (
            aws_sdk_application_discovery_service.types.order_string.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrderByElement:
    out: OrderByElement = {}  # type: ignore[typeddict-item]
    if "fieldName" in data:
        out["field_name"] = data["fieldName"]
    else:
        raise DeserializationError("OrderByElement.field_name required")
    if "sortOrder" in data:
        import aws_sdk_application_discovery_service.types.order_string

        out["sort_order"] = (
            aws_sdk_application_discovery_service.types.order_string.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    return out
