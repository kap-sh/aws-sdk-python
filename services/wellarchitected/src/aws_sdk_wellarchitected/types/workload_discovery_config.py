"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadDiscoveryConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.trusted_advisor_integration_status
    import aws_sdk_wellarchitected.types.workload_resource_definition


class WorkloadDiscoveryConfig(TypedDict):
    trusted_advisor_integration_status: NotRequired[
        "aws_sdk_wellarchitected.types.trusted_advisor_integration_status.TrustedAdvisorIntegrationStatus"
    ]
    """<p>Discovery integration status in respect to Trusted Advisor for the workload.</p>"""
    workload_resource_definition: NotRequired[
        "aws_sdk_wellarchitected.types.workload_resource_definition.WorkloadResourceDefinition"
    ]
    """<p>The mode to use for identifying resources associated with the workload.</p> <p>You can specify <code>WORKLOAD_METADATA</code>, <code>APP_REGISTRY</code>, or both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadDiscoveryConfig) -> dict:
    out: dict = {}
    if "trusted_advisor_integration_status" in value:
        import aws_sdk_wellarchitected.types.trusted_advisor_integration_status

        out["TrustedAdvisorIntegrationStatus"] = (
            aws_sdk_wellarchitected.types.trusted_advisor_integration_status.serialize_json(
                value["trusted_advisor_integration_status"]
            )
        )
    if "workload_resource_definition" in value:
        import aws_sdk_wellarchitected.types.workload_resource_definition

        out["WorkloadResourceDefinition"] = (
            aws_sdk_wellarchitected.types.workload_resource_definition.serialize_json(
                value["workload_resource_definition"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkloadDiscoveryConfig:
    out: WorkloadDiscoveryConfig = {}  # type: ignore[typeddict-item]
    if "TrustedAdvisorIntegrationStatus" in data:
        import aws_sdk_wellarchitected.types.trusted_advisor_integration_status

        out["trusted_advisor_integration_status"] = (
            aws_sdk_wellarchitected.types.trusted_advisor_integration_status.deserialize_json(
                data["TrustedAdvisorIntegrationStatus"]
            )
        )
    if "WorkloadResourceDefinition" in data:
        import aws_sdk_wellarchitected.types.workload_resource_definition

        out["workload_resource_definition"] = (
            aws_sdk_wellarchitected.types.workload_resource_definition.deserialize_json(
                data["WorkloadResourceDefinition"]
            )
        )
    return out
