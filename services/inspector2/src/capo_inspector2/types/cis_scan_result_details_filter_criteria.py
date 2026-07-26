"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultDetailsFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.check_id_filter_list
    import capo_inspector2.types.cis_finding_arn_filter_list
    import capo_inspector2.types.cis_finding_status_filter_list
    import capo_inspector2.types.cis_security_level_filter_list
    import capo_inspector2.types.title_filter_list


class CisScanResultDetailsFilterCriteria(TypedDict, closed=True):
    finding_status_filters: NotRequired[
        "capo_inspector2.types.cis_finding_status_filter_list.CisFindingStatusFilterList"
    ]
    """<p>The criteria's finding status filters.</p>"""
    check_id_filters: NotRequired[
        "capo_inspector2.types.check_id_filter_list.CheckIdFilterList"
    ]
    """<p>The criteria's check ID filters.</p>"""
    title_filters: NotRequired[
        "capo_inspector2.types.title_filter_list.TitleFilterList"
    ]
    """<p>The criteria's title filters.</p>"""
    security_level_filters: NotRequired[
        "capo_inspector2.types.cis_security_level_filter_list.CisSecurityLevelFilterList"
    ]
    """<p> The criteria's security level filters. . Security level refers to the Benchmark levels that CIS assigns to a profile. </p>"""
    finding_arn_filters: NotRequired[
        "capo_inspector2.types.cis_finding_arn_filter_list.CisFindingArnFilterList"
    ]
    """<p>The criteria's finding ARN filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisScanResultDetailsFilterCriteria) -> dict:
    out: dict = {}
    if "finding_status_filters" in value:
        import capo_inspector2.types.cis_finding_status_filter_list

        out["findingStatusFilters"] = (
            capo_inspector2.types.cis_finding_status_filter_list.serialize_json(
                value["finding_status_filters"]
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
    if "security_level_filters" in value:
        import capo_inspector2.types.cis_security_level_filter_list

        out["securityLevelFilters"] = (
            capo_inspector2.types.cis_security_level_filter_list.serialize_json(
                value["security_level_filters"]
            )
        )
    if "finding_arn_filters" in value:
        import capo_inspector2.types.cis_finding_arn_filter_list

        out["findingArnFilters"] = (
            capo_inspector2.types.cis_finding_arn_filter_list.serialize_json(
                value["finding_arn_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> CisScanResultDetailsFilterCriteria:
    out: CisScanResultDetailsFilterCriteria = {}  # type: ignore[typeddict-item]
    if "findingStatusFilters" in data:
        import capo_inspector2.types.cis_finding_status_filter_list

        out["finding_status_filters"] = (
            capo_inspector2.types.cis_finding_status_filter_list.deserialize_json(
                data["findingStatusFilters"]
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
    if "securityLevelFilters" in data:
        import capo_inspector2.types.cis_security_level_filter_list

        out["security_level_filters"] = (
            capo_inspector2.types.cis_security_level_filter_list.deserialize_json(
                data["securityLevelFilters"]
            )
        )
    if "findingArnFilters" in data:
        import capo_inspector2.types.cis_finding_arn_filter_list

        out["finding_arn_filters"] = (
            capo_inspector2.types.cis_finding_arn_filter_list.deserialize_json(
                data["findingArnFilters"]
            )
        )
    return out
