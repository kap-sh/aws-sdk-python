"""Generated from Smithy shape ``com.amazonaws.pinpoint#PhoneNumberValidateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.number_validate_request


class PhoneNumberValidateRequest(TypedDict, closed=True):
    number_validate_request: NotRequired[
        "capo_pinpoint.types.number_validate_request.NumberValidateRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberValidateRequest) -> dict:
    out: dict = {}
    if "number_validate_request" in value:
        import capo_pinpoint.types.number_validate_request

        out["NumberValidateRequest"] = (
            capo_pinpoint.types.number_validate_request.serialize_json(
                value["number_validate_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> PhoneNumberValidateRequest:
    out: PhoneNumberValidateRequest = {}  # type: ignore[typeddict-item]
    if "NumberValidateRequest" in data:
        import capo_pinpoint.types.number_validate_request

        out["number_validate_request"] = (
            capo_pinpoint.types.number_validate_request.deserialize_json(
                data["NumberValidateRequest"]
            )
        )
    return out
