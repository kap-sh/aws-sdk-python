"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEventTypesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.event_type_list
    import aws_sdk_frauddetector.types.string


class GetEventTypesResult(TypedDict, closed=True):
    event_types: NotRequired[
        "aws_sdk_frauddetector.types.event_type_list.eventTypeList"
    ]
    """<p>An array of event types.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next page token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventTypesResult) -> dict:
    out: dict = {}
    if "event_types" in value:
        import aws_sdk_frauddetector.types.event_type_list

        out["eventTypes"] = (
            aws_sdk_frauddetector.types.event_type_list.serialize_aws_json_1_1(
                value["event_types"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventTypesResult:
    out: GetEventTypesResult = {}  # type: ignore[typeddict-item]
    if "eventTypes" in data:
        import aws_sdk_frauddetector.types.event_type_list

        out["event_types"] = (
            aws_sdk_frauddetector.types.event_type_list.deserialize_aws_json_1_1(
                data["eventTypes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
