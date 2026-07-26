"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetAppsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.applications_response


class GetAppsResponse(TypedDict, closed=True):
    applications_response: NotRequired[
        "capo_pinpoint.types.applications_response.ApplicationsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetAppsResponse) -> dict:
    out: dict = {}
    if "applications_response" in value:
        import capo_pinpoint.types.applications_response

        out["ApplicationsResponse"] = (
            capo_pinpoint.types.applications_response.serialize_json(
                value["applications_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAppsResponse:
    out: GetAppsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationsResponse" in data:
        import capo_pinpoint.types.applications_response

        out["applications_response"] = (
            capo_pinpoint.types.applications_response.deserialize_json(
                data["ApplicationsResponse"]
            )
        )
    return out
