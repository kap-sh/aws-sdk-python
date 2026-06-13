"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormInputBindingPropertiesValueProperties``."""

from typing import TypedDict

from typing_extensions import NotRequired


class FormInputBindingPropertiesValueProperties(TypedDict):
    model: NotRequired["str"]
    """<p>An Amplify DataStore model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInputBindingPropertiesValueProperties) -> dict:
    out: dict = {}
    if "model" in value:
        out["model"] = value["model"]
    return out


def deserialize_json(data: dict) -> FormInputBindingPropertiesValueProperties:
    out: FormInputBindingPropertiesValueProperties = {}  # type: ignore[typeddict-item]
    if "model" in data:
        out["model"] = data["model"]
    return out
