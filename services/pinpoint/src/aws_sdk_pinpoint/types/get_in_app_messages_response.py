"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetInAppMessagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.in_app_messages_response


class GetInAppMessagesResponse(TypedDict, closed=True):
    in_app_messages_response: NotRequired[
        "aws_sdk_pinpoint.types.in_app_messages_response.InAppMessagesResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetInAppMessagesResponse) -> dict:
    out: dict = {}
    if "in_app_messages_response" in value:
        import aws_sdk_pinpoint.types.in_app_messages_response

        out["InAppMessagesResponse"] = (
            aws_sdk_pinpoint.types.in_app_messages_response.serialize_json(
                value["in_app_messages_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetInAppMessagesResponse:
    out: GetInAppMessagesResponse = {}  # type: ignore[typeddict-item]
    if "InAppMessagesResponse" in data:
        import aws_sdk_pinpoint.types.in_app_messages_response

        out["in_app_messages_response"] = (
            aws_sdk_pinpoint.types.in_app_messages_response.deserialize_json(
                data["InAppMessagesResponse"]
            )
        )
    return out
