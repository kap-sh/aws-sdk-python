"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component


class UpdateComponentResponse(TypedDict, closed=True):
    entity: NotRequired["aws_sdk_amplifyuibuilder.types.component.Component"]
    """<p>Describes the configuration of the updated component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateComponentResponse) -> dict:
    out: dict = {}
    if "entity" in value:
        import aws_sdk_amplifyuibuilder.types.component

        out["entity"] = aws_sdk_amplifyuibuilder.types.component.serialize_json(
            value["entity"]
        )
    return out


def deserialize_json(data: dict) -> UpdateComponentResponse:
    out: UpdateComponentResponse = {}  # type: ignore[typeddict-item]
    if "entity" in data:
        import aws_sdk_amplifyuibuilder.types.component

        out["entity"] = aws_sdk_amplifyuibuilder.types.component.deserialize_json(
            data["entity"]
        )
    return out
