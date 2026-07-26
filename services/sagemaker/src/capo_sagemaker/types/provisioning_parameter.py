"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProvisioningParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.provisioning_parameter_key
    import capo_sagemaker.types.provisioning_parameter_value


class ProvisioningParameter(TypedDict, closed=True):
    key: NotRequired[
        "capo_sagemaker.types.provisioning_parameter_key.ProvisioningParameterKey"
    ]
    """<p>The key that identifies a provisioning parameter.</p>"""
    value: NotRequired[
        "capo_sagemaker.types.provisioning_parameter_value.ProvisioningParameterValue"
    ]
    """<p>The value of the provisioning parameter.</p>"""


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
