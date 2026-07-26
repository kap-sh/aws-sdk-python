"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.resource_category
    import capo_securityhub.types.resource_config
    import capo_securityhub.types.resource_findings_summary_list
    import capo_securityhub.types.resource_tag_list


class ResourceResult(TypedDict, closed=True):
    resource_guid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The global identifier used to identify a resource.</p>"""
    resource_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier for a resource.</p>"""
    account_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services account that owns the resource.</p>"""
    region: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services Region where the resource is located.</p>"""
    resource_category: NotRequired[
        "capo_securityhub.types.resource_category.ResourceCategory"
    ]
    """<p>The grouping where the resource belongs.</p>"""
    resource_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of resource.</p>"""
    resource_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the resource.</p>"""
    resource_creation_time_dt: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The time when the resource was created.</p>"""
    resource_detail_capture_time_dt: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The timestamp when information about the resource was captured.</p>"""
    findings_summary: NotRequired[
        "capo_securityhub.types.resource_findings_summary_list.ResourceFindingsSummaryList"
    ]
    """<p>An aggregated view of security findings associated with a resource.</p>"""
    resource_tags: NotRequired[
        "capo_securityhub.types.resource_tag_list.ResourceTagList"
    ]
    """<p>The key-value pairs associated with a resource.</p>"""
    resource_config: NotRequired[
        "capo_securityhub.types.resource_config.ResourceConfig"
    ]
    """<p>The configuration details of a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceResult) -> dict:
    out: dict = {}
    if "resource_guid" in value:
        out["ResourceGuid"] = value["resource_guid"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "region" in value:
        out["Region"] = value["region"]
    if "resource_category" in value:
        import capo_securityhub.types.resource_category

        out["ResourceCategory"] = (
            capo_securityhub.types.resource_category.serialize_json(
                value["resource_category"]
            )
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "resource_creation_time_dt" in value:
        out["ResourceCreationTimeDt"] = value["resource_creation_time_dt"]
    if "resource_detail_capture_time_dt" in value:
        out["ResourceDetailCaptureTimeDt"] = value["resource_detail_capture_time_dt"]
    if "findings_summary" in value:
        import capo_securityhub.types.resource_findings_summary_list

        out["FindingsSummary"] = (
            capo_securityhub.types.resource_findings_summary_list.serialize_json(
                value["findings_summary"]
            )
        )
    if "resource_tags" in value:
        import capo_securityhub.types.resource_tag_list

        out["ResourceTags"] = capo_securityhub.types.resource_tag_list.serialize_json(
            value["resource_tags"]
        )
    if "resource_config" in value:
        out["ResourceConfig"] = value["resource_config"]
    return out


def deserialize_json(data: dict) -> ResourceResult:
    out: ResourceResult = {}  # type: ignore[typeddict-item]
    if "ResourceGuid" in data:
        out["resource_guid"] = data["ResourceGuid"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "ResourceCategory" in data:
        import capo_securityhub.types.resource_category

        out["resource_category"] = (
            capo_securityhub.types.resource_category.deserialize_json(
                data["ResourceCategory"]
            )
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    if "ResourceCreationTimeDt" in data:
        out["resource_creation_time_dt"] = data["ResourceCreationTimeDt"]
    if "ResourceDetailCaptureTimeDt" in data:
        out["resource_detail_capture_time_dt"] = data["ResourceDetailCaptureTimeDt"]
    if "FindingsSummary" in data:
        import capo_securityhub.types.resource_findings_summary_list

        out["findings_summary"] = (
            capo_securityhub.types.resource_findings_summary_list.deserialize_json(
                data["FindingsSummary"]
            )
        )
    if "ResourceTags" in data:
        import capo_securityhub.types.resource_tag_list

        out["resource_tags"] = (
            capo_securityhub.types.resource_tag_list.deserialize_json(
                data["ResourceTags"]
            )
        )
    if "ResourceConfig" in data:
        out["resource_config"] = data["ResourceConfig"]
    return out
