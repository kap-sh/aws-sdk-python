"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetFormResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.form


class GetFormResponse(TypedDict, closed=True):
    form: NotRequired["capo_amplifyuibuilder.types.form.Form"]
    """<p>Represents the configuration settings for the form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFormResponse) -> dict:
    out: dict = {}
    if "form" in value:
        import capo_amplifyuibuilder.types.form

        out["form"] = capo_amplifyuibuilder.types.form.serialize_json(value["form"])
    return out


def deserialize_json(data: dict) -> GetFormResponse:
    out: GetFormResponse = {}  # type: ignore[typeddict-item]
    if "form" in data:
        import capo_amplifyuibuilder.types.form

        out["form"] = capo_amplifyuibuilder.types.form.deserialize_json(data["form"])
    return out
