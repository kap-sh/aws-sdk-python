"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.application_response


class GetAppResponse(TypedDict, closed=True):
    application_response: NotRequired[
        "aws_sdk_pinpoint.types.application_response.ApplicationResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetAppResponse) -> dict:
    out: dict = {}
    if "application_response" in value:
        import aws_sdk_pinpoint.types.application_response

        out["ApplicationResponse"] = (
            aws_sdk_pinpoint.types.application_response.serialize_json(
                value["application_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAppResponse:
    out: GetAppResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationResponse" in data:
        import aws_sdk_pinpoint.types.application_response

        out["application_response"] = (
            aws_sdk_pinpoint.types.application_response.deserialize_json(
                data["ApplicationResponse"]
            )
        )
    return out
