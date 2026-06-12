"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateJourneyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.write_journey_request


class CreateJourneyRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    write_journey_request: NotRequired[
        "aws_sdk_pinpoint.types.write_journey_request.WriteJourneyRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateJourneyRequest) -> dict:
    out: dict = {}
    if "write_journey_request" in value:
        import aws_sdk_pinpoint.types.write_journey_request

        out["WriteJourneyRequest"] = (
            aws_sdk_pinpoint.types.write_journey_request.serialize_json(
                value["write_journey_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateJourneyRequest:
    out: CreateJourneyRequest = {}  # type: ignore[typeddict-item]
    if "WriteJourneyRequest" in data:
        import aws_sdk_pinpoint.types.write_journey_request

        out["write_journey_request"] = (
            aws_sdk_pinpoint.types.write_journey_request.deserialize_json(
                data["WriteJourneyRequest"]
            )
        )
    return out
