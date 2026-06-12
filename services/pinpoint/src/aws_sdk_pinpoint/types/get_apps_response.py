"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetAppsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.applications_response


class GetAppsResponse(TypedDict):
    applications_response: NotRequired[
        "aws_sdk_pinpoint.types.applications_response.ApplicationsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetAppsResponse) -> dict:
    out: dict = {}
    if "applications_response" in value:
        import aws_sdk_pinpoint.types.applications_response

        out["ApplicationsResponse"] = (
            aws_sdk_pinpoint.types.applications_response.serialize_json(
                value["applications_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAppsResponse:
    out: GetAppsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationsResponse" in data:
        import aws_sdk_pinpoint.types.applications_response

        out["applications_response"] = (
            aws_sdk_pinpoint.types.applications_response.deserialize_json(
                data["ApplicationsResponse"]
            )
        )
    return out
