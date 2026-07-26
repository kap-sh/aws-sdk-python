"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ResourceSnapshotPayload``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_opportunity_summary_full_view
    import capo_partnercentral_selling.types.opportunity_summary_view


class _ResourceSnapshotPayload_OpportunitySummary(TypedDict, closed=True):
    OpportunitySummary: "capo_partnercentral_selling.types.opportunity_summary_view.OpportunitySummaryView"


class _ResourceSnapshotPayload_AwsOpportunitySummaryFullView(TypedDict, closed=True):
    AwsOpportunitySummaryFullView: "capo_partnercentral_selling.types.aws_opportunity_summary_full_view.AwsOpportunitySummaryFullView"


ResourceSnapshotPayload: TypeAlias = (
    _ResourceSnapshotPayload_OpportunitySummary
    | _ResourceSnapshotPayload_AwsOpportunitySummaryFullView
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSnapshotPayload) -> dict:
    if "OpportunitySummary" in value:
        import capo_partnercentral_selling.types.opportunity_summary_view

        return {
            "OpportunitySummary": capo_partnercentral_selling.types.opportunity_summary_view.serialize_aws_json_1_0(
                value["OpportunitySummary"]
            )
        }
    elif "AwsOpportunitySummaryFullView" in value:
        import capo_partnercentral_selling.types.aws_opportunity_summary_full_view

        return {
            "AwsOpportunitySummaryFullView": capo_partnercentral_selling.types.aws_opportunity_summary_full_view.serialize_aws_json_1_0(
                value["AwsOpportunitySummaryFullView"]
            )
        }
    else:
        raise SerializationError("ResourceSnapshotPayload: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ResourceSnapshotPayload:
    if "OpportunitySummary" in data:
        import capo_partnercentral_selling.types.opportunity_summary_view

        return {
            "OpportunitySummary": capo_partnercentral_selling.types.opportunity_summary_view.deserialize_aws_json_1_0(
                data["OpportunitySummary"]
            )
        }
    elif "AwsOpportunitySummaryFullView" in data:
        import capo_partnercentral_selling.types.aws_opportunity_summary_full_view

        return {
            "AwsOpportunitySummaryFullView": capo_partnercentral_selling.types.aws_opportunity_summary_full_view.deserialize_aws_json_1_0(
                data["AwsOpportunitySummaryFullView"]
            )
        }
    else:
        raise DeserializationError("ResourceSnapshotPayload: no recognized variant key")
