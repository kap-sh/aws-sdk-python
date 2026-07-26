"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateServiceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service


class CreateServiceResponse(TypedDict, closed=True):
    service: "capo_resiliencehubv2.types.service.Service"
    """<p>The created service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.service

    out["service"] = capo_resiliencehubv2.types.service.serialize_json(value["service"])
    return out


def deserialize_json(data: dict) -> CreateServiceResponse:
    out: CreateServiceResponse = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import capo_resiliencehubv2.types.service

        out["service"] = capo_resiliencehubv2.types.service.deserialize_json(
            data["service"]
        )
    else:
        raise DeserializationError("CreateServiceResponse.service required")
    return out
