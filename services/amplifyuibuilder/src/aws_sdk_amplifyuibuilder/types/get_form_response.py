"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetFormResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.form


class GetFormResponse(TypedDict):
    form: NotRequired["aws_sdk_amplifyuibuilder.types.form.Form"]
    """<p>Represents the configuration settings for the form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFormResponse) -> dict:
    out: dict = {}
    if "form" in value:
        import aws_sdk_amplifyuibuilder.types.form

        out["form"] = aws_sdk_amplifyuibuilder.types.form.serialize_json(value["form"])
    return out


def deserialize_json(data: dict) -> GetFormResponse:
    out: GetFormResponse = {}  # type: ignore[typeddict-item]
    if "form" in data:
        import aws_sdk_amplifyuibuilder.types.form

        out["form"] = aws_sdk_amplifyuibuilder.types.form.deserialize_json(data["form"])
    return out
