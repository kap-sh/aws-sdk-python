"""Generated from Smithy shape ``com.amazonaws.pinpoint#RemoveAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.update_attributes_request


class RemoveAttributesRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    attribute_type: "capo_pinpoint.types.__string.__string"
    """<p>The type of attribute or attributes to remove. Valid values are:</p> <ul><li><p>endpoint-custom-attributes - Custom attributes that describe endpoints, such as the date when an associated user opted in or out of receiving communications from you through a specific type of channel.</p></li> <li><p>endpoint-metric-attributes - Custom metrics that your app reports to Amazon Pinpoint for endpoints, such as the number of app sessions or the number of items left in a cart.</p></li> <li><p>endpoint-user-attributes - Custom attributes that describe users, such as first name, last name, and age.</p></li></ul>"""
    update_attributes_request: NotRequired[
        "capo_pinpoint.types.update_attributes_request.UpdateAttributesRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RemoveAttributesRequest) -> dict:
    out: dict = {}
    if "update_attributes_request" in value:
        import capo_pinpoint.types.update_attributes_request

        out["UpdateAttributesRequest"] = (
            capo_pinpoint.types.update_attributes_request.serialize_json(
                value["update_attributes_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemoveAttributesRequest:
    out: RemoveAttributesRequest = {}  # type: ignore[typeddict-item]
    if "UpdateAttributesRequest" in data:
        import capo_pinpoint.types.update_attributes_request

        out["update_attributes_request"] = (
            capo_pinpoint.types.update_attributes_request.deserialize_json(
                data["UpdateAttributesRequest"]
            )
        )
    return out
