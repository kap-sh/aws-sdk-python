"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.parameter_key
    import capo_service_catalog.types.parameter_value


class ProvisioningParameter(TypedDict, closed=True):
    key: NotRequired["capo_service_catalog.types.parameter_key.ParameterKey"]
    """<p>The parameter key.</p>"""
    value: NotRequired["capo_service_catalog.types.parameter_value.ParameterValue"]
    """<p>The parameter value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningParameter:
    out: ProvisioningParameter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
