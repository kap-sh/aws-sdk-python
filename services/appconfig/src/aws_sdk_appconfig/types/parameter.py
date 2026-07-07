"""Generated from Smithy shape ``com.amazonaws.appconfig#Parameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.boolean
    import aws_sdk_appconfig.types.description


class Parameter(TypedDict, closed=True):
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>Information about the parameter.</p>"""
    required: "aws_sdk_appconfig.types.boolean.Boolean"
    """<p>A parameter value must be specified in the extension association.</p>"""
    dynamic: "aws_sdk_appconfig.types.boolean.Boolean"
    """<p>Indicates whether this parameter's value can be supplied at the extension's action point instead of during extension association. Dynamic parameters can't be marked <code>Required</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Parameter) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["Required"] = value.get("required", False)
    out["Dynamic"] = value.get("dynamic", False)
    return out


def deserialize_json(data: dict) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Required" in data:
        out["required"] = data["Required"]
    else:
        out["required"] = False
    if "Dynamic" in data:
        out["dynamic"] = data["Dynamic"]
    else:
        out["dynamic"] = False
    return out
