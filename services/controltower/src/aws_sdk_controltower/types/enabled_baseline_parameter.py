"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_baseline_parameter_document


class EnabledBaselineParameter(TypedDict, closed=True):
    key: "str"
    """<p>A string denoting the parameter key.</p>"""
    value: "aws_sdk_controltower.types.enabled_baseline_parameter_document.EnabledBaselineParameterDocument"
    """<p>A low-level <code>Document</code> object of any type (for example, a Java Object).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineParameter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EnabledBaselineParameter:
    out: EnabledBaselineParameter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("EnabledBaselineParameter.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("EnabledBaselineParameter.value required")
    return out
