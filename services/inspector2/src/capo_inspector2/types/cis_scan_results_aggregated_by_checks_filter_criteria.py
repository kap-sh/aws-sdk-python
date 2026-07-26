"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultsAggregatedByChecksFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.check_id_filter_list
    import capo_inspector2.types.cis_number_filter_list
    import capo_inspector2.types.cis_security_level_filter_list
    import capo_inspector2.types.one_account_id_filter_list
    import capo_inspector2.types.platform_filter_list
    import capo_inspector2.types.title_filter_list


class CisScanResultsAggregatedByChecksFilterCriteria(TypedDict, closed=True):
    account_id_filters: NotRequired[
        "capo_inspector2.types.one_account_id_filter_list.OneAccountIdFilterList"
    ]
    """<p>The criteria's account ID filters.</p>"""
    check_id_filters: NotRequired[
        "capo_inspector2.types.check_id_filter_list.CheckIdFilterList"
    ]
    """<p>The criteria's check ID filters.</p>"""
    title_filters: NotRequired[
        "capo_inspector2.types.title_filter_list.TitleFilterList"
    ]
    """<p>The criteria's title filters.</p>"""
    platform_filters: NotRequired[
        "capo_inspector2.types.platform_filter_list.PlatformFilterList"
    ]
    """<p>The criteria's platform filters.</p>"""
    failed_resources_filters: NotRequired[
        "capo_inspector2.types.cis_number_filter_list.CisNumberFilterList"
    ]
    """<p>The criteria's failed resources filters.</p>"""
    security_level_filters: NotRequired[
        "capo_inspector2.types.cis_security_level_filter_list.CisSecurityLevelFilterList"
    ]
    """<p>The criteria's security level filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisScanResultsAggregatedByChecksFilterCriteria) -> dict:
    out: dict = {}
    if "account_id_filters" in value:
        import capo_inspector2.types.one_account_id_filter_list

        out["accountIdFilters"] = (
            capo_inspector2.types.one_account_id_filter_list.serialize_json(
                value["account_id_filters"]
            )
        )
    if "check_id_filters" in value:
        import capo_inspector2.types.check_id_filter_list

        out["checkIdFilters"] = (
            capo_inspector2.types.check_id_filter_list.serialize_json(
                value["check_id_filters"]
            )
        )
    if "title_filters" in value:
        import capo_inspector2.types.title_filter_list

        out["titleFilters"] = capo_inspector2.types.title_filter_list.serialize_json(
            value["title_filters"]
        )
    if "platform_filters" in value:
        import capo_inspector2.types.platform_filter_list

        out["platformFilters"] = (
            capo_inspector2.types.platform_filter_list.serialize_json(
                value["platform_filters"]
            )
        )
    if "failed_resources_filters" in value:
        import capo_inspector2.types.cis_number_filter_list

        out["failedResourcesFilters"] = (
            capo_inspector2.types.cis_number_filter_list.serialize_json(
                value["failed_resources_filters"]
            )
        )
    if "security_level_filters" in value:
        import capo_inspector2.types.cis_security_level_filter_list

        out["securityLevelFilters"] = (
            capo_inspector2.types.cis_security_level_filter_list.serialize_json(
                value["security_level_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> CisScanResultsAggregatedByChecksFilterCriteria:
    out: CisScanResultsAggregatedByChecksFilterCriteria = {}  # type: ignore[typeddict-item]
    if "accountIdFilters" in data:
        import capo_inspector2.types.one_account_id_filter_list

        out["account_id_filters"] = (
            capo_inspector2.types.one_account_id_filter_list.deserialize_json(
                data["accountIdFilters"]
            )
        )
    if "checkIdFilters" in data:
        import capo_inspector2.types.check_id_filter_list

        out["check_id_filters"] = (
            capo_inspector2.types.check_id_filter_list.deserialize_json(
                data["checkIdFilters"]
            )
        )
    if "titleFilters" in data:
        import capo_inspector2.types.title_filter_list

        out["title_filters"] = capo_inspector2.types.title_filter_list.deserialize_json(
            data["titleFilters"]
        )
    if "platformFilters" in data:
        import capo_inspector2.types.platform_filter_list

        out["platform_filters"] = (
            capo_inspector2.types.platform_filter_list.deserialize_json(
                data["platformFilters"]
            )
        )
    if "failedResourcesFilters" in data:
        import capo_inspector2.types.cis_number_filter_list

        out["failed_resources_filters"] = (
            capo_inspector2.types.cis_number_filter_list.deserialize_json(
                data["failedResourcesFilters"]
            )
        )
    if "securityLevelFilters" in data:
        import capo_inspector2.types.cis_security_level_filter_list

        out["security_level_filters"] = (
            capo_inspector2.types.cis_security_level_filter_list.deserialize_json(
                data["securityLevelFilters"]
            )
        )
    return out
