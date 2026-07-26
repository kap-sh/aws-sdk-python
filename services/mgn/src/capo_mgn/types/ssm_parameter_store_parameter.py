"""Generated from Smithy shape ``com.amazonaws.mgn#SsmParameterStoreParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.ssm_parameter_store_parameter_name
    import capo_mgn.types.ssm_parameter_store_parameter_type


class SsmParameterStoreParameter(TypedDict, closed=True):
    parameter_type: "capo_mgn.types.ssm_parameter_store_parameter_type.SsmParameterStoreParameterType"
    """<p>AWS Systems Manager Parameter Store parameter type.</p>"""
    parameter_name: "capo_mgn.types.ssm_parameter_store_parameter_name.SsmParameterStoreParameterName"
    """<p>AWS Systems Manager Parameter Store parameter name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsmParameterStoreParameter) -> dict:
    out: dict = {}
    out["parameterType"] = value["parameter_type"]
    out["parameterName"] = value["parameter_name"]
    return out


def deserialize_json(data: dict) -> SsmParameterStoreParameter:
    out: SsmParameterStoreParameter = {}  # type: ignore[typeddict-item]
    if "parameterType" in data:
        out["parameter_type"] = data["parameterType"]
    else:
        raise DeserializationError("SsmParameterStoreParameter.parameter_type required")
    if "parameterName" in data:
        out["parameter_name"] = data["parameterName"]
    else:
        raise DeserializationError("SsmParameterStoreParameter.parameter_name required")
    return out
