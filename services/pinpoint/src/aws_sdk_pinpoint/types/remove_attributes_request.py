"""Generated from Smithy shape ``com.amazonaws.pinpoint#RemoveAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.update_attributes_request


class RemoveAttributesRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    attribute_type: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The type of attribute or attributes to remove. Valid values are:</p> <ul><li><p>endpoint-custom-attributes - Custom attributes that describe endpoints, such as the date when an associated user opted in or out of receiving communications from you through a specific type of channel.</p></li> <li><p>endpoint-metric-attributes - Custom metrics that your app reports to Amazon Pinpoint for endpoints, such as the number of app sessions or the number of items left in a cart.</p></li> <li><p>endpoint-user-attributes - Custom attributes that describe users, such as first name, last name, and age.</p></li></ul>"""
    update_attributes_request: NotRequired[
        "aws_sdk_pinpoint.types.update_attributes_request.UpdateAttributesRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RemoveAttributesRequest) -> dict:
    out: dict = {}
    if "update_attributes_request" in value:
        import aws_sdk_pinpoint.types.update_attributes_request

        out["UpdateAttributesRequest"] = (
            aws_sdk_pinpoint.types.update_attributes_request.serialize_json(
                value["update_attributes_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemoveAttributesRequest:
    out: RemoveAttributesRequest = {}  # type: ignore[typeddict-item]
    if "UpdateAttributesRequest" in data:
        import aws_sdk_pinpoint.types.update_attributes_request

        out["update_attributes_request"] = (
            aws_sdk_pinpoint.types.update_attributes_request.deserialize_json(
                data["UpdateAttributesRequest"]
            )
        )
    return out
