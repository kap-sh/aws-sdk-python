"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationOverview``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_status_aggregated_count
    import aws_sdk_ssm.types.status_name


class AssociationOverview(TypedDict):
    status: NotRequired["aws_sdk_ssm.types.status_name.StatusName"]
    """<p>The status of the association. Status can be: Pending, Success, or Failed.</p>"""
    detailed_status: NotRequired["aws_sdk_ssm.types.status_name.StatusName"]
    """<p>A detailed status of the association.</p>"""
    association_status_aggregated_count: NotRequired[
        "aws_sdk_ssm.types.association_status_aggregated_count.AssociationStatusAggregatedCount"
    ]
    """<p>Returns the number of targets for the association status. For example, if you created an association with two managed nodes, and one of them was successful, this would return the count of managed nodes by status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationOverview) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "detailed_status" in value:
        out["DetailedStatus"] = value["detailed_status"]
    if "association_status_aggregated_count" in value:
        import aws_sdk_ssm.types.association_status_aggregated_count

        out["AssociationStatusAggregatedCount"] = (
            aws_sdk_ssm.types.association_status_aggregated_count.serialize_aws_json_1_1(
                value["association_status_aggregated_count"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationOverview:
    out: AssociationOverview = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    if "DetailedStatus" in data:
        out["detailed_status"] = data["DetailedStatus"]
    if "AssociationStatusAggregatedCount" in data:
        import aws_sdk_ssm.types.association_status_aggregated_count

        out["association_status_aggregated_count"] = (
            aws_sdk_ssm.types.association_status_aggregated_count.deserialize_aws_json_1_1(
                data["AssociationStatusAggregatedCount"]
            )
        )
    return out
