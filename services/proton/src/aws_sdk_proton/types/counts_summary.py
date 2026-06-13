"""Generated from Smithy shape ``com.amazonaws.proton#CountsSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_counts_summary


class CountsSummary(TypedDict):
    components: NotRequired[
        "aws_sdk_proton.types.resource_counts_summary.ResourceCountsSummary"
    ]
    """<p>The total number of components in the Amazon Web Services account.</p> <p>The semantics of the <code>components</code> field are different from the semantics of results for other infrastructure-provisioning resources. That's because at this time components don't have associated templates, therefore they don't have the concept of staleness. The <code>components</code> object will only contain <code>total</code> and <code>failed</code> members.</p>"""
    environments: NotRequired[
        "aws_sdk_proton.types.resource_counts_summary.ResourceCountsSummary"
    ]
    """<p>The staleness counts for Proton environments in the Amazon Web Services account. The <code>environments</code> object will only contain <code>total</code> members.</p>"""
    environment_templates: NotRequired[
        "aws_sdk_proton.types.resource_counts_summary.ResourceCountsSummary"
    ]
    """<p>The total number of environment templates in the Amazon Web Services account. The <code>environmentTemplates</code> object will only contain <code>total</code> members.</p>"""
    service_instances: NotRequired[
        "aws_sdk_proton.types.resource_counts_summary.ResourceCountsSummary"
    ]
    """<p>The staleness counts for Proton service instances in the Amazon Web Services account.</p>"""
    services: NotRequired[
        "aws_sdk_proton.types.resource_counts_summary.ResourceCountsSummary"
    ]
    """<p>The staleness counts for Proton services in the Amazon Web Services account.</p>"""
    service_templates: NotRequired[
        "aws_sdk_proton.types.resource_counts_summary.ResourceCountsSummary"
    ]
    """<p>The total number of service templates in the Amazon Web Services account. The <code>serviceTemplates</code> object will only contain <code>total</code> members.</p>"""
    pipelines: NotRequired[
        "aws_sdk_proton.types.resource_counts_summary.ResourceCountsSummary"
    ]
    """<p>The staleness counts for Proton pipelines in the Amazon Web Services account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountsSummary) -> dict:
    out: dict = {}
    if "components" in value:
        import aws_sdk_proton.types.resource_counts_summary

        out["components"] = (
            aws_sdk_proton.types.resource_counts_summary.serialize_aws_json_1_0(
                value["components"]
            )
        )
    if "environments" in value:
        import aws_sdk_proton.types.resource_counts_summary

        out["environments"] = (
            aws_sdk_proton.types.resource_counts_summary.serialize_aws_json_1_0(
                value["environments"]
            )
        )
    if "environment_templates" in value:
        import aws_sdk_proton.types.resource_counts_summary

        out["environmentTemplates"] = (
            aws_sdk_proton.types.resource_counts_summary.serialize_aws_json_1_0(
                value["environment_templates"]
            )
        )
    if "service_instances" in value:
        import aws_sdk_proton.types.resource_counts_summary

        out["serviceInstances"] = (
            aws_sdk_proton.types.resource_counts_summary.serialize_aws_json_1_0(
                value["service_instances"]
            )
        )
    if "services" in value:
        import aws_sdk_proton.types.resource_counts_summary

        out["services"] = (
            aws_sdk_proton.types.resource_counts_summary.serialize_aws_json_1_0(
                value["services"]
            )
        )
    if "service_templates" in value:
        import aws_sdk_proton.types.resource_counts_summary

        out["serviceTemplates"] = (
            aws_sdk_proton.types.resource_counts_summary.serialize_aws_json_1_0(
                value["service_templates"]
            )
        )
    if "pipelines" in value:
        import aws_sdk_proton.types.resource_counts_summary

        out["pipelines"] = (
            aws_sdk_proton.types.resource_counts_summary.serialize_aws_json_1_0(
                value["pipelines"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CountsSummary:
    out: CountsSummary = {}  # type: ignore[typeddict-item]
    if "components" in data:
        import aws_sdk_proton.types.resource_counts_summary

        out["components"] = (
            aws_sdk_proton.types.resource_counts_summary.deserialize_aws_json_1_0(
                data["components"]
            )
        )
    if "environments" in data:
        import aws_sdk_proton.types.resource_counts_summary

        out["environments"] = (
            aws_sdk_proton.types.resource_counts_summary.deserialize_aws_json_1_0(
                data["environments"]
            )
        )
    if "environmentTemplates" in data:
        import aws_sdk_proton.types.resource_counts_summary

        out["environment_templates"] = (
            aws_sdk_proton.types.resource_counts_summary.deserialize_aws_json_1_0(
                data["environmentTemplates"]
            )
        )
    if "serviceInstances" in data:
        import aws_sdk_proton.types.resource_counts_summary

        out["service_instances"] = (
            aws_sdk_proton.types.resource_counts_summary.deserialize_aws_json_1_0(
                data["serviceInstances"]
            )
        )
    if "services" in data:
        import aws_sdk_proton.types.resource_counts_summary

        out["services"] = (
            aws_sdk_proton.types.resource_counts_summary.deserialize_aws_json_1_0(
                data["services"]
            )
        )
    if "serviceTemplates" in data:
        import aws_sdk_proton.types.resource_counts_summary

        out["service_templates"] = (
            aws_sdk_proton.types.resource_counts_summary.deserialize_aws_json_1_0(
                data["serviceTemplates"]
            )
        )
    if "pipelines" in data:
        import aws_sdk_proton.types.resource_counts_summary

        out["pipelines"] = (
            aws_sdk_proton.types.resource_counts_summary.deserialize_aws_json_1_0(
                data["pipelines"]
            )
        )
    return out
