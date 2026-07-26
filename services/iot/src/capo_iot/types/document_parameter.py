"""Generated from Smithy shape ``com.amazonaws.iot#DocumentParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.example
    import capo_iot.types.job_description
    import capo_iot.types.optional
    import capo_iot.types.parameter_key
    import capo_iot.types.regex


class DocumentParameter(TypedDict, closed=True):
    key: NotRequired["capo_iot.types.parameter_key.ParameterKey"]
    """<p>Key of the map field containing the patterns that need to be replaced in a managed template job document schema.</p>"""
    description: NotRequired["capo_iot.types.job_description.JobDescription"]
    """<p>Description of the map field containing the patterns that need to be replaced in a managed template job document schema.</p>"""
    regex: NotRequired["capo_iot.types.regex.Regex"]
    """<p>A regular expression of the patterns that need to be replaced in a managed template job document schema.</p>"""
    example: NotRequired["capo_iot.types.example.Example"]
    """<p>An example illustrating a pattern that need to be replaced in a managed template job document schema.</p>"""
    optional: "capo_iot.types.optional.Optional"
    """<p>Specifies whether a pattern that needs to be replaced in a managed template job document schema is optional or required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "description" in value:
        out["description"] = value["description"]
    if "regex" in value:
        out["regex"] = value["regex"]
    if "example" in value:
        out["example"] = value["example"]
    out["optional"] = value.get("optional", False)
    return out


def deserialize_json(data: dict) -> DocumentParameter:
    out: DocumentParameter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "description" in data:
        out["description"] = data["description"]
    if "regex" in data:
        out["regex"] = data["regex"]
    if "example" in data:
        out["example"] = data["example"]
    if "optional" in data:
        out["optional"] = data["optional"]
    else:
        out["optional"] = False
    return out
