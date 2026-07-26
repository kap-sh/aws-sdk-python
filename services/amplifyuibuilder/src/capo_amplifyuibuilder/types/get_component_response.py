"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component


class GetComponentResponse(TypedDict, closed=True):
    component: NotRequired["capo_amplifyuibuilder.types.component.Component"]
    """<p>Represents the configuration settings for the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentResponse) -> dict:
    out: dict = {}
    if "component" in value:
        import capo_amplifyuibuilder.types.component

        out["component"] = capo_amplifyuibuilder.types.component.serialize_json(
            value["component"]
        )
    return out


def deserialize_json(data: dict) -> GetComponentResponse:
    out: GetComponentResponse = {}  # type: ignore[typeddict-item]
    if "component" in data:
        import capo_amplifyuibuilder.types.component

        out["component"] = capo_amplifyuibuilder.types.component.deserialize_json(
            data["component"]
        )
    return out
