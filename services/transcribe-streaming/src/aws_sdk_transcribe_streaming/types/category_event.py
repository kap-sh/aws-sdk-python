"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#CategoryEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transcribe_streaming._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.matched_category_details
    import aws_sdk_transcribe_streaming.types.string_list


class CategoryEvent(TypedDict, closed=True):
    matched_categories: NotRequired[
        "aws_sdk_transcribe_streaming.types.string_list.StringList"
    ]
    """<p>Lists the categories that were matched in your audio segment.</p>"""
    matched_details: NotRequired[
        "aws_sdk_transcribe_streaming.types.matched_category_details.MatchedCategoryDetails"
    ]
    """<p>Contains information about the matched categories, including category names and timestamps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryEvent) -> dict:
    out: dict = {}
    if "matched_categories" in value:
        import aws_sdk_transcribe_streaming.types.string_list

        out["MatchedCategories"] = (
            aws_sdk_transcribe_streaming.types.string_list.serialize_json(
                value["matched_categories"]
            )
        )
    if "matched_details" in value:
        import aws_sdk_transcribe_streaming.types.matched_category_details

        out["MatchedDetails"] = (
            aws_sdk_transcribe_streaming.types.matched_category_details.serialize_json(
                value["matched_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CategoryEvent:
    out: CategoryEvent = {}  # type: ignore[typeddict-item]
    if "MatchedCategories" in data:
        import aws_sdk_transcribe_streaming.types.string_list

        out["matched_categories"] = (
            aws_sdk_transcribe_streaming.types.string_list.deserialize_json(
                data["MatchedCategories"]
            )
        )
    if "MatchedDetails" in data:
        import aws_sdk_transcribe_streaming.types.matched_category_details

        out["matched_details"] = (
            aws_sdk_transcribe_streaming.types.matched_category_details.deserialize_json(
                data["MatchedDetails"]
            )
        )
    return out


def serialize_event_json(value: CategoryEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "CategoryEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> CategoryEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: CategoryEvent = {}  # type: ignore[typeddict-item]
    return out
