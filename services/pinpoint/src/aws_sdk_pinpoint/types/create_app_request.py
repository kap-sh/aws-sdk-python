"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.create_application_request


class CreateAppRequest(TypedDict, closed=True):
    create_application_request: NotRequired[
        "aws_sdk_pinpoint.types.create_application_request.CreateApplicationRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppRequest) -> dict:
    out: dict = {}
    if "create_application_request" in value:
        import aws_sdk_pinpoint.types.create_application_request

        out["CreateApplicationRequest"] = (
            aws_sdk_pinpoint.types.create_application_request.serialize_json(
                value["create_application_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAppRequest:
    out: CreateAppRequest = {}  # type: ignore[typeddict-item]
    if "CreateApplicationRequest" in data:
        import aws_sdk_pinpoint.types.create_application_request

        out["create_application_request"] = (
            aws_sdk_pinpoint.types.create_application_request.deserialize_json(
                data["CreateApplicationRequest"]
            )
        )
    return out
