"""Generated from Smithy shape ``com.amazonaws.location#DeleteRouteCalculatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.resource_name


class DeleteRouteCalculatorRequest(TypedDict, closed=True):
    calculator_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the route calculator resource to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouteCalculatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRouteCalculatorRequest:
    out: DeleteRouteCalculatorRequest = {}  # type: ignore[typeddict-item]
    return out
