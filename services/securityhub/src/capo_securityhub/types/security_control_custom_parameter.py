"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlCustomParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.parameters


class SecurityControlCustomParameter(TypedDict, closed=True):
    security_control_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the security control. </p>"""
    parameters: NotRequired["capo_securityhub.types.parameters.Parameters"]
    """<p> An object that specifies parameter values for a control in a configuration policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlCustomParameter) -> dict:
    out: dict = {}
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "parameters" in value:
        import capo_securityhub.types.parameters

        out["Parameters"] = capo_securityhub.types.parameters.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> SecurityControlCustomParameter:
    out: SecurityControlCustomParameter = {}  # type: ignore[typeddict-item]
    if "SecurityControlId" in data:
        out["security_control_id"] = data["SecurityControlId"]
    if "Parameters" in data:
        import capo_securityhub.types.parameters

        out["parameters"] = capo_securityhub.types.parameters.deserialize_json(
            data["Parameters"]
        )
    return out
