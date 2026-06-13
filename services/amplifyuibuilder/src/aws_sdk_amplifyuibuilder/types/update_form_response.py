"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateFormResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.form


class UpdateFormResponse(TypedDict):
    entity: NotRequired["aws_sdk_amplifyuibuilder.types.form.Form"]
    """<p>Describes the configuration of the updated form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFormResponse) -> dict:
    out: dict = {}
    if "entity" in value:
        import aws_sdk_amplifyuibuilder.types.form

        out["entity"] = aws_sdk_amplifyuibuilder.types.form.serialize_json(
            value["entity"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFormResponse:
    out: UpdateFormResponse = {}  # type: ignore[typeddict-item]
    if "entity" in data:
        import aws_sdk_amplifyuibuilder.types.form

        out["entity"] = aws_sdk_amplifyuibuilder.types.form.deserialize_json(
            data["entity"]
        )
    return out
