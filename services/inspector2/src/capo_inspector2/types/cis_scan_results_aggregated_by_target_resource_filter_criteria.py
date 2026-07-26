"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultsAggregatedByTargetResourceFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id_filter_list
    import capo_inspector2.types.check_id_filter_list
    import capo_inspector2.types.cis_number_filter_list
    import capo_inspector2.types.cis_result_status_filter_list
    import capo_inspector2.types.platform_filter_list
    import capo_inspector2.types.resource_id_filter_list
    import capo_inspector2.types.resource_tag_filter_list
    import capo_inspector2.types.target_status_filter_list
    import capo_inspector2.types.target_status_reason_filter_list


class CisScanResultsAggregatedByTargetResourceFilterCriteria(TypedDict, closed=True):
    account_id_filters: NotRequired[
        "capo_inspector2.types.account_id_filter_list.AccountIdFilterList"
    ]
    """<p>The criteria's account ID filters.</p>"""
    status_filters: NotRequired[
        "capo_inspector2.types.cis_result_status_filter_list.CisResultStatusFilterList"
    ]
    """<p>The criteria's status filter.</p>"""
    check_id_filters: NotRequired[
        "capo_inspector2.types.check_id_filter_list.CheckIdFilterList"
    ]
    """<p>The criteria's check ID filters.</p>"""
    target_resource_id_filters: NotRequired[
        "capo_inspector2.types.resource_id_filter_list.ResourceIdFilterList"
    ]
    """<p>The criteria's target resource ID filters.</p>"""
    target_resource_tag_filters: NotRequired[
        "capo_inspector2.types.resource_tag_filter_list.ResourceTagFilterList"
    ]
    """<p>The criteria's target resource tag filters.</p>"""
    platform_filters: NotRequired[
        "capo_inspector2.types.platform_filter_list.PlatformFilterList"
    ]
    """<p>The criteria's platform filters.</p>"""
    target_status_filters: NotRequired[
        "capo_inspector2.types.target_status_filter_list.TargetStatusFilterList"
    ]
    """<p>The criteria's target status filters.</p>"""
    target_status_reason_filters: NotRequired[
        "capo_inspector2.types.target_status_reason_filter_list.TargetStatusReasonFilterList"
    ]
    """<p>The criteria's target status reason filters.</p>"""
    failed_checks_filters: NotRequired[
        "capo_inspector2.types.cis_number_filter_list.CisNumberFilterList"
    ]
    """<p>The criteria's failed checks filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: CisScanResultsAggregatedByTargetResourceFilterCriteria,
) -> dict:
    out: dict = {}
    if "account_id_filters" in value:
        import capo_inspector2.types.account_id_filter_list

        out["accountIdFilters"] = (
            capo_inspector2.types.account_id_filter_list.serialize_json(
                value["account_id_filters"]
            )
        )
    if "status_filters" in value:
        import capo_inspector2.types.cis_result_status_filter_list

        out["statusFilters"] = (
            capo_inspector2.types.cis_result_status_filter_list.serialize_json(
                value["status_filters"]
            )
        )
    if "check_id_filters" in value:
        import capo_inspector2.types.check_id_filter_list

        out["checkIdFilters"] = (
            capo_inspector2.types.check_id_filter_list.serialize_json(
                value["check_id_filters"]
            )
        )
    if "target_resource_id_filters" in value:
        import capo_inspector2.types.resource_id_filter_list

        out["targetResourceIdFilters"] = (
            capo_inspector2.types.resource_id_filter_list.serialize_json(
                value["target_resource_id_filters"]
            )
        )
    if "target_resource_tag_filters" in value:
        import capo_inspector2.types.resource_tag_filter_list

        out["targetResourceTagFilters"] = (
            capo_inspector2.types.resource_tag_filter_list.serialize_json(
                value["target_resource_tag_filters"]
            )
        )
    if "platform_filters" in value:
        import capo_inspector2.types.platform_filter_list

        out["platformFilters"] = (
            capo_inspector2.types.platform_filter_list.serialize_json(
                value["platform_filters"]
            )
        )
    if "target_status_filters" in value:
        import capo_inspector2.types.target_status_filter_list

        out["targetStatusFilters"] = (
            capo_inspector2.types.target_status_filter_list.serialize_json(
                value["target_status_filters"]
            )
        )
    if "target_status_reason_filters" in value:
        import capo_inspector2.types.target_status_reason_filter_list

        out["targetStatusReasonFilters"] = (
            capo_inspector2.types.target_status_reason_filter_list.serialize_json(
                value["target_status_reason_filters"]
            )
        )
    if "failed_checks_filters" in value:
        import capo_inspector2.types.cis_number_filter_list

        out["failedChecksFilters"] = (
            capo_inspector2.types.cis_number_filter_list.serialize_json(
                value["failed_checks_filters"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> CisScanResultsAggregatedByTargetResourceFilterCriteria:
    out: CisScanResultsAggregatedByTargetResourceFilterCriteria = {}  # type: ignore[typeddict-item]
    if "accountIdFilters" in data:
        import capo_inspector2.types.account_id_filter_list

        out["account_id_filters"] = (
            capo_inspector2.types.account_id_filter_list.deserialize_json(
                data["accountIdFilters"]
            )
        )
    if "statusFilters" in data:
        import capo_inspector2.types.cis_result_status_filter_list

        out["status_filters"] = (
            capo_inspector2.types.cis_result_status_filter_list.deserialize_json(
                data["statusFilters"]
            )
        )
    if "checkIdFilters" in data:
        import capo_inspector2.types.check_id_filter_list

        out["check_id_filters"] = (
            capo_inspector2.types.check_id_filter_list.deserialize_json(
                data["checkIdFilters"]
            )
        )
    if "targetResourceIdFilters" in data:
        import capo_inspector2.types.resource_id_filter_list

        out["target_resource_id_filters"] = (
            capo_inspector2.types.resource_id_filter_list.deserialize_json(
                data["targetResourceIdFilters"]
            )
        )
    if "targetResourceTagFilters" in data:
        import capo_inspector2.types.resource_tag_filter_list

        out["target_resource_tag_filters"] = (
            capo_inspector2.types.resource_tag_filter_list.deserialize_json(
                data["targetResourceTagFilters"]
            )
        )
    if "platformFilters" in data:
        import capo_inspector2.types.platform_filter_list

        out["platform_filters"] = (
            capo_inspector2.types.platform_filter_list.deserialize_json(
                data["platformFilters"]
            )
        )
    if "targetStatusFilters" in data:
        import capo_inspector2.types.target_status_filter_list

        out["target_status_filters"] = (
            capo_inspector2.types.target_status_filter_list.deserialize_json(
                data["targetStatusFilters"]
            )
        )
    if "targetStatusReasonFilters" in data:
        import capo_inspector2.types.target_status_reason_filter_list

        out["target_status_reason_filters"] = (
            capo_inspector2.types.target_status_reason_filter_list.deserialize_json(
                data["targetStatusReasonFilters"]
            )
        )
    if "failedChecksFilters" in data:
        import capo_inspector2.types.cis_number_filter_list

        out["failed_checks_filters"] = (
            capo_inspector2.types.cis_number_filter_list.deserialize_json(
                data["failedChecksFilters"]
            )
        )
    return out
