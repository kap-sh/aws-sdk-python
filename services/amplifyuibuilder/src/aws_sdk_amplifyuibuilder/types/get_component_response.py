"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetComponentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component


class GetComponentResponse(TypedDict):
    component: NotRequired["aws_sdk_amplifyuibuilder.types.component.Component"]
    """<p>Represents the configuration settings for the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentResponse) -> dict:
    out: dict = {}
    if "component" in value:
        import aws_sdk_amplifyuibuilder.types.component

        out["component"] = aws_sdk_amplifyuibuilder.types.component.serialize_json(
            value["component"]
        )
    return out


def deserialize_json(data: dict) -> GetComponentResponse:
    out: GetComponentResponse = {}  # type: ignore[typeddict-item]
    if "component" in data:
        import aws_sdk_amplifyuibuilder.types.component

        out["component"] = aws_sdk_amplifyuibuilder.types.component.deserialize_json(
            data["component"]
        )
    return out
