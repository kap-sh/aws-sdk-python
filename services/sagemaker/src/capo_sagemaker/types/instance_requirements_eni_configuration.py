"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceRequirementsEniConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.additional_enis


class InstanceRequirementsEniConfiguration(TypedDict, closed=True):
    customer_eni: NotRequired["str"]
    """<p>The ID of the customer-managed Elastic Network Interface (ENI) associated with the instance type category.</p>"""
    additional_enis: NotRequired["capo_sagemaker.types.additional_enis.AdditionalEnis"]
    """<p>Information about additional Elastic Network Interfaces (ENIs) associated with the instance type category.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceRequirementsEniConfiguration) -> dict:
    out: dict = {}
    if "customer_eni" in value:
        out["CustomerEni"] = value["customer_eni"]
    if "additional_enis" in value:
        import capo_sagemaker.types.additional_enis

        out["AdditionalEnis"] = (
            capo_sagemaker.types.additional_enis.serialize_aws_json_1_1(
                value["additional_enis"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceRequirementsEniConfiguration:
    out: InstanceRequirementsEniConfiguration = {}  # type: ignore[typeddict-item]
    if "CustomerEni" in data:
        out["customer_eni"] = data["CustomerEni"]
    if "AdditionalEnis" in data:
        import capo_sagemaker.types.additional_enis

        out["additional_enis"] = (
            capo_sagemaker.types.additional_enis.deserialize_aws_json_1_1(
                data["AdditionalEnis"]
            )
        )
    return out
