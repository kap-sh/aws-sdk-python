"""Generated from Smithy shape ``com.amazonaws.sesv2#GetSuppressedDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.suppressed_destination


class GetSuppressedDestinationResponse(TypedDict, closed=True):
    suppressed_destination: (
        "capo_sesv2.types.suppressed_destination.SuppressedDestination"
    )
    """<p>An object containing information about the suppressed email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSuppressedDestinationResponse) -> dict:
    out: dict = {}
    import capo_sesv2.types.suppressed_destination

    out["SuppressedDestination"] = (
        capo_sesv2.types.suppressed_destination.serialize_json(
            value["suppressed_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetSuppressedDestinationResponse:
    out: GetSuppressedDestinationResponse = {}  # type: ignore[typeddict-item]
    if "SuppressedDestination" in data:
        import capo_sesv2.types.suppressed_destination

        out["suppressed_destination"] = (
            capo_sesv2.types.suppressed_destination.deserialize_json(
                data["SuppressedDestination"]
            )
        )
    else:
        raise DeserializationError(
            "GetSuppressedDestinationResponse.suppressed_destination required"
        )
    return out
