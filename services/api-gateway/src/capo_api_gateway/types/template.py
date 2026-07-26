"""Generated from Smithy shape ``com.amazonaws.apigateway#Template``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class Template(TypedDict, closed=True):
    value: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The Apache Velocity Template Language (VTL) template content used for the template resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Template) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Template:
    out: Template = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    return out
