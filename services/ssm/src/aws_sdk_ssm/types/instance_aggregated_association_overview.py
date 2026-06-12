"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceAggregatedAssociationOverview``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_association_status_aggregated_count
    import aws_sdk_ssm.types.status_name


class InstanceAggregatedAssociationOverview(TypedDict):
    detailed_status: NotRequired["aws_sdk_ssm.types.status_name.StatusName"]
    """<p>Detailed status information about the aggregated associations.</p>"""
    instance_association_status_aggregated_count: NotRequired[
        "aws_sdk_ssm.types.instance_association_status_aggregated_count.InstanceAssociationStatusAggregatedCount"
    ]
    """<p>The number of associations for the managed nodes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAggregatedAssociationOverview) -> dict:
    out: dict = {}
    if "detailed_status" in value:
        out["DetailedStatus"] = value["detailed_status"]
    if "instance_association_status_aggregated_count" in value:
        import aws_sdk_ssm.types.instance_association_status_aggregated_count

        out["InstanceAssociationStatusAggregatedCount"] = (
            aws_sdk_ssm.types.instance_association_status_aggregated_count.serialize_aws_json_1_1(
                value["instance_association_status_aggregated_count"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAggregatedAssociationOverview:
    out: InstanceAggregatedAssociationOverview = {}  # type: ignore[typeddict-item]
    if "DetailedStatus" in data:
        out["detailed_status"] = data["DetailedStatus"]
    if "InstanceAssociationStatusAggregatedCount" in data:
        import aws_sdk_ssm.types.instance_association_status_aggregated_count

        out["instance_association_status_aggregated_count"] = (
            aws_sdk_ssm.types.instance_association_status_aggregated_count.deserialize_aws_json_1_1(
                data["InstanceAssociationStatusAggregatedCount"]
            )
        )
    return out
