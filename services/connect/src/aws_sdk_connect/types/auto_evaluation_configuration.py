"""Generated from Smithy shape ``com.amazonaws.connect#AutoEvaluationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean


class AutoEvaluationConfiguration(TypedDict):
    enabled: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Whether automated evaluations are enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoEvaluationConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> AutoEvaluationConfiguration:
    out: AutoEvaluationConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
