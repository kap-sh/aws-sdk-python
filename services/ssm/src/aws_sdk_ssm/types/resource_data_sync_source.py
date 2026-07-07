"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_aws_organizations_source
    import aws_sdk_ssm.types.resource_data_sync_enable_all_ops_data_sources
    import aws_sdk_ssm.types.resource_data_sync_include_future_regions
    import aws_sdk_ssm.types.resource_data_sync_source_region_list
    import aws_sdk_ssm.types.resource_data_sync_source_type


class ResourceDataSyncSource(TypedDict, closed=True):
    source_type: (
        "aws_sdk_ssm.types.resource_data_sync_source_type.ResourceDataSyncSourceType"
    )
    """<p>The type of data source for the resource data sync. <code>SourceType</code> is either <code>AwsOrganizations</code> (if an organization is present in Organizations) or <code>SingleAccountMultiRegions</code>.</p>"""
    aws_organizations_source: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_aws_organizations_source.ResourceDataSyncAwsOrganizationsSource"
    ]
    """<p>Information about the <code>AwsOrganizationsSource</code> resource data sync source. A sync source of this type can synchronize data from Organizations.</p>"""
    source_regions: "aws_sdk_ssm.types.resource_data_sync_source_region_list.ResourceDataSyncSourceRegionList"
    """<p>The <code>SyncSource</code> Amazon Web Services Regions included in the resource data sync.</p>"""
    include_future_regions: "aws_sdk_ssm.types.resource_data_sync_include_future_regions.ResourceDataSyncIncludeFutureRegions"
    """<p>Whether to automatically synchronize and aggregate data from new Amazon Web Services Regions when those Regions come online.</p>"""
    enable_all_ops_data_sources: "aws_sdk_ssm.types.resource_data_sync_enable_all_ops_data_sources.ResourceDataSyncEnableAllOpsDataSources"
    r"""<p>When you create a resource data sync, if you choose one of the Organizations options, then Systems Manager automatically enables all OpsData sources in the selected Amazon Web Services Regions for all Amazon Web Services accounts in your organization (or in the selected organization units). For more information, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html\">Setting up Systems Manager Explorer to display data from multiple accounts and Regions</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncSource) -> dict:
    out: dict = {}
    out["SourceType"] = value["source_type"]
    if "aws_organizations_source" in value:
        import aws_sdk_ssm.types.resource_data_sync_aws_organizations_source

        out["AwsOrganizationsSource"] = (
            aws_sdk_ssm.types.resource_data_sync_aws_organizations_source.serialize_aws_json_1_1(
                value["aws_organizations_source"]
            )
        )
    import aws_sdk_ssm.types.resource_data_sync_source_region_list

    out["SourceRegions"] = (
        aws_sdk_ssm.types.resource_data_sync_source_region_list.serialize_aws_json_1_1(
            value["source_regions"]
        )
    )
    out["IncludeFutureRegions"] = value.get("include_future_regions", False)
    out["EnableAllOpsDataSources"] = value.get("enable_all_ops_data_sources", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncSource:
    out: ResourceDataSyncSource = {}  # type: ignore[typeddict-item]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    else:
        raise DeserializationError("ResourceDataSyncSource.source_type required")
    if "AwsOrganizationsSource" in data:
        import aws_sdk_ssm.types.resource_data_sync_aws_organizations_source

        out["aws_organizations_source"] = (
            aws_sdk_ssm.types.resource_data_sync_aws_organizations_source.deserialize_aws_json_1_1(
                data["AwsOrganizationsSource"]
            )
        )
    if "SourceRegions" in data:
        import aws_sdk_ssm.types.resource_data_sync_source_region_list

        out["source_regions"] = (
            aws_sdk_ssm.types.resource_data_sync_source_region_list.deserialize_aws_json_1_1(
                data["SourceRegions"]
            )
        )
    else:
        raise DeserializationError("ResourceDataSyncSource.source_regions required")
    if "IncludeFutureRegions" in data:
        out["include_future_regions"] = data["IncludeFutureRegions"]
    else:
        out["include_future_regions"] = False
    if "EnableAllOpsDataSources" in data:
        out["enable_all_ops_data_sources"] = data["EnableAllOpsDataSources"]
    else:
        out["enable_all_ops_data_sources"] = False
    return out
