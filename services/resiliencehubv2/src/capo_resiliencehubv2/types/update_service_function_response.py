"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateServiceFunctionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_function


class UpdateServiceFunctionResponse(TypedDict, closed=True):
    service_function: "capo_resiliencehubv2.types.service_function.ServiceFunction"
    """<p>The updated service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceFunctionResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.service_function

    out["serviceFunction"] = capo_resiliencehubv2.types.service_function.serialize_json(
        value["service_function"]
    )
    return out


def deserialize_json(data: dict) -> UpdateServiceFunctionResponse:
    out: UpdateServiceFunctionResponse = {}  # type: ignore[typeddict-item]
    if "serviceFunction" in data:
        import capo_resiliencehubv2.types.service_function

        out["service_function"] = (
            capo_resiliencehubv2.types.service_function.deserialize_json(
                data["serviceFunction"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceFunctionResponse.service_function required"
        )
    return out
