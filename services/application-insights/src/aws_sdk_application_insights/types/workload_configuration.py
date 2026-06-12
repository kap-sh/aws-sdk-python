"""Generated from Smithy shape ``com.amazonaws.applicationinsights#WorkloadConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.component_configuration
    import aws_sdk_application_insights.types.tier
    import aws_sdk_application_insights.types.workload_name


class WorkloadConfiguration(TypedDict):
    workload_name: NotRequired[
        "aws_sdk_application_insights.types.workload_name.WorkloadName"
    ]
    """<p>The name of the workload.</p>"""
    tier: NotRequired["aws_sdk_application_insights.types.tier.Tier"]
    """<p>The configuration of the workload tier.</p>"""
    configuration: NotRequired[
        "aws_sdk_application_insights.types.component_configuration.ComponentConfiguration"
    ]
    """<p>The configuration settings of the workload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkloadConfiguration) -> dict:
    out: dict = {}
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "tier" in value:
        import aws_sdk_application_insights.types.tier

        out["Tier"] = aws_sdk_application_insights.types.tier.serialize_aws_json_1_1(
            value["tier"]
        )
    if "configuration" in value:
        out["Configuration"] = value["configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkloadConfiguration:
    out: WorkloadConfiguration = {}  # type: ignore[typeddict-item]
    if "WorkloadName" in data:
        out["workload_name"] = data["WorkloadName"]
    if "Tier" in data:
        import aws_sdk_application_insights.types.tier

        out["tier"] = aws_sdk_application_insights.types.tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    if "Configuration" in data:
        out["configuration"] = data["Configuration"]
    return out
