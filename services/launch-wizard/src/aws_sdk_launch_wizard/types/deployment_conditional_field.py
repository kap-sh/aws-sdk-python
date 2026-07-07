"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentConditionalField``."""

from typing_extensions import NotRequired, TypedDict


class DeploymentConditionalField(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the deployment condition.</p>"""
    value: NotRequired["str"]
    """<p>The value of the condition.</p>"""
    comparator: NotRequired["str"]
    """<p>The comparator of the condition.</p> <p>Valid values: <code>Equal | NotEqual</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentConditionalField) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    if "comparator" in value:
        out["comparator"] = value["comparator"]
    return out


def deserialize_json(data: dict) -> DeploymentConditionalField:
    out: DeploymentConditionalField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    if "comparator" in data:
        out["comparator"] = data["comparator"]
    return out
