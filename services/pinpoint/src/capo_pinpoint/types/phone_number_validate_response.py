"""Generated from Smithy shape ``com.amazonaws.pinpoint#PhoneNumberValidateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.number_validate_response


class PhoneNumberValidateResponse(TypedDict, closed=True):
    number_validate_response: NotRequired[
        "capo_pinpoint.types.number_validate_response.NumberValidateResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberValidateResponse) -> dict:
    out: dict = {}
    if "number_validate_response" in value:
        import capo_pinpoint.types.number_validate_response

        out["NumberValidateResponse"] = (
            capo_pinpoint.types.number_validate_response.serialize_json(
                value["number_validate_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> PhoneNumberValidateResponse:
    out: PhoneNumberValidateResponse = {}  # type: ignore[typeddict-item]
    if "NumberValidateResponse" in data:
        import capo_pinpoint.types.number_validate_response

        out["number_validate_response"] = (
            capo_pinpoint.types.number_validate_response.deserialize_json(
                data["NumberValidateResponse"]
            )
        )
    return out
