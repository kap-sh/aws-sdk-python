"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.additional_enis
    import aws_sdk_sagemaker.types.capacity_reservation
    import aws_sdk_sagemaker.types.cluster_node_logical_id
    import aws_sdk_sagemaker.types.instance_requirements_eni_configurations


class InstanceMetadata(TypedDict, closed=True):
    customer_eni: NotRequired["str"]
    """<p>The ID of the customer-managed Elastic Network Interface (ENI) associated with the instance.</p>"""
    additional_enis: NotRequired[
        "aws_sdk_sagemaker.types.additional_enis.AdditionalEnis"
    ]
    """<p>Information about additional Elastic Network Interfaces (ENIs) associated with the instance.</p>"""
    instance_requirements_eni_configurations: NotRequired[
        "aws_sdk_sagemaker.types.instance_requirements_eni_configurations.InstanceRequirementsEniConfigurations"
    ]
    """<p>The ENI configurations for the instance types in the instance requirements, grouped by network interface category (for example, ENI-only or EFA with ENIs). At most one configuration per category.</p>"""
    capacity_reservation: NotRequired[
        "aws_sdk_sagemaker.types.capacity_reservation.CapacityReservation"
    ]
    """<p>Information about the Capacity Reservation used by the instance.</p>"""
    failure_message: NotRequired["str"]
    """<p>An error message describing why the instance creation or update failed, if applicable.</p>"""
    lcs_execution_state: NotRequired["str"]
    """<p>The execution state of the Lifecycle Script (LCS) for the instance.</p>"""
    node_logical_id: NotRequired[
        "aws_sdk_sagemaker.types.cluster_node_logical_id.ClusterNodeLogicalId"
    ]
    """<p>The unique logical identifier of the node within the cluster. The ID used here is the same object as in the <code>BatchAddClusterNodes</code> API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceMetadata) -> dict:
    out: dict = {}
    if "customer_eni" in value:
        out["CustomerEni"] = value["customer_eni"]
    if "additional_enis" in value:
        import aws_sdk_sagemaker.types.additional_enis

        out["AdditionalEnis"] = (
            aws_sdk_sagemaker.types.additional_enis.serialize_aws_json_1_1(
                value["additional_enis"]
            )
        )
    if "instance_requirements_eni_configurations" in value:
        import aws_sdk_sagemaker.types.instance_requirements_eni_configurations

        out["InstanceRequirementsEniConfigurations"] = (
            aws_sdk_sagemaker.types.instance_requirements_eni_configurations.serialize_aws_json_1_1(
                value["instance_requirements_eni_configurations"]
            )
        )
    if "capacity_reservation" in value:
        import aws_sdk_sagemaker.types.capacity_reservation

        out["CapacityReservation"] = (
            aws_sdk_sagemaker.types.capacity_reservation.serialize_aws_json_1_1(
                value["capacity_reservation"]
            )
        )
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "lcs_execution_state" in value:
        out["LcsExecutionState"] = value["lcs_execution_state"]
    if "node_logical_id" in value:
        out["NodeLogicalId"] = value["node_logical_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceMetadata:
    out: InstanceMetadata = {}  # type: ignore[typeddict-item]
    if "CustomerEni" in data:
        out["customer_eni"] = data["CustomerEni"]
    if "AdditionalEnis" in data:
        import aws_sdk_sagemaker.types.additional_enis

        out["additional_enis"] = (
            aws_sdk_sagemaker.types.additional_enis.deserialize_aws_json_1_1(
                data["AdditionalEnis"]
            )
        )
    if "InstanceRequirementsEniConfigurations" in data:
        import aws_sdk_sagemaker.types.instance_requirements_eni_configurations

        out["instance_requirements_eni_configurations"] = (
            aws_sdk_sagemaker.types.instance_requirements_eni_configurations.deserialize_aws_json_1_1(
                data["InstanceRequirementsEniConfigurations"]
            )
        )
    if "CapacityReservation" in data:
        import aws_sdk_sagemaker.types.capacity_reservation

        out["capacity_reservation"] = (
            aws_sdk_sagemaker.types.capacity_reservation.deserialize_aws_json_1_1(
                data["CapacityReservation"]
            )
        )
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "LcsExecutionState" in data:
        out["lcs_execution_state"] = data["LcsExecutionState"]
    if "NodeLogicalId" in data:
        out["node_logical_id"] = data["NodeLogicalId"]
    return out
