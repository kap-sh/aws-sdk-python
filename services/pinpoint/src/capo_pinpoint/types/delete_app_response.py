"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.application_response


class DeleteAppResponse(TypedDict, closed=True):
    application_response: NotRequired[
        "capo_pinpoint.types.application_response.ApplicationResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppResponse) -> dict:
    out: dict = {}
    if "application_response" in value:
        import capo_pinpoint.types.application_response

        out["ApplicationResponse"] = (
            capo_pinpoint.types.application_response.serialize_json(
                value["application_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteAppResponse:
    out: DeleteAppResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationResponse" in data:
        import capo_pinpoint.types.application_response

        out["application_response"] = (
            capo_pinpoint.types.application_response.deserialize_json(
                data["ApplicationResponse"]
            )
        )
    return out
