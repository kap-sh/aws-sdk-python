"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultDetailsFilterCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.check_id_filter_list
    import aws_sdk_inspector2.types.cis_finding_arn_filter_list
    import aws_sdk_inspector2.types.cis_finding_status_filter_list
    import aws_sdk_inspector2.types.cis_security_level_filter_list
    import aws_sdk_inspector2.types.title_filter_list


class CisScanResultDetailsFilterCriteria(TypedDict):
    finding_status_filters: NotRequired[
        "aws_sdk_inspector2.types.cis_finding_status_filter_list.CisFindingStatusFilterList"
    ]
    """<p>The criteria's finding status filters.</p>"""
    check_id_filters: NotRequired[
        "aws_sdk_inspector2.types.check_id_filter_list.CheckIdFilterList"
    ]
    """<p>The criteria's check ID filters.</p>"""
    title_filters: NotRequired[
        "aws_sdk_inspector2.types.title_filter_list.TitleFilterList"
    ]
    """<p>The criteria's title filters.</p>"""
    security_level_filters: NotRequired[
        "aws_sdk_inspector2.types.cis_security_level_filter_list.CisSecurityLevelFilterList"
    ]
    """<p> The criteria's security level filters. . Security level refers to the Benchmark levels that CIS assigns to a profile. </p>"""
    finding_arn_filters: NotRequired[
        "aws_sdk_inspector2.types.cis_finding_arn_filter_list.CisFindingArnFilterList"
    ]
    """<p>The criteria's finding ARN filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisScanResultDetailsFilterCriteria) -> dict:
    out: dict = {}
    if "finding_status_filters" in value:
        import aws_sdk_inspector2.types.cis_finding_status_filter_list

        out["findingStatusFilters"] = (
            aws_sdk_inspector2.types.cis_finding_status_filter_list.serialize_json(
                value["finding_status_filters"]
            )
        )
    if "check_id_filters" in value:
        import aws_sdk_inspector2.types.check_id_filter_list

        out["checkIdFilters"] = (
            aws_sdk_inspector2.types.check_id_filter_list.serialize_json(
                value["check_id_filters"]
            )
        )
    if "title_filters" in value:
        import aws_sdk_inspector2.types.title_filter_list

        out["titleFilters"] = aws_sdk_inspector2.types.title_filter_list.serialize_json(
            value["title_filters"]
        )
    if "security_level_filters" in value:
        import aws_sdk_inspector2.types.cis_security_level_filter_list

        out["securityLevelFilters"] = (
            aws_sdk_inspector2.types.cis_security_level_filter_list.serialize_json(
                value["security_level_filters"]
            )
        )
    if "finding_arn_filters" in value:
        import aws_sdk_inspector2.types.cis_finding_arn_filter_list

        out["findingArnFilters"] = (
            aws_sdk_inspector2.types.cis_finding_arn_filter_list.serialize_json(
                value["finding_arn_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> CisScanResultDetailsFilterCriteria:
    out: CisScanResultDetailsFilterCriteria = {}  # type: ignore[typeddict-item]
    if "findingStatusFilters" in data:
        import aws_sdk_inspector2.types.cis_finding_status_filter_list

        out["finding_status_filters"] = (
            aws_sdk_inspector2.types.cis_finding_status_filter_list.deserialize_json(
                data["findingStatusFilters"]
            )
        )
    if "checkIdFilters" in data:
        import aws_sdk_inspector2.types.check_id_filter_list

        out["check_id_filters"] = (
            aws_sdk_inspector2.types.check_id_filter_list.deserialize_json(
                data["checkIdFilters"]
            )
        )
    if "titleFilters" in data:
        import aws_sdk_inspector2.types.title_filter_list

        out["title_filters"] = (
            aws_sdk_inspector2.types.title_filter_list.deserialize_json(
                data["titleFilters"]
            )
        )
    if "securityLevelFilters" in data:
        import aws_sdk_inspector2.types.cis_security_level_filter_list

        out["security_level_filters"] = (
            aws_sdk_inspector2.types.cis_security_level_filter_list.deserialize_json(
                data["securityLevelFilters"]
            )
        )
    if "findingArnFilters" in data:
        import aws_sdk_inspector2.types.cis_finding_arn_filter_list

        out["finding_arn_filters"] = (
            aws_sdk_inspector2.types.cis_finding_arn_filter_list.deserialize_json(
                data["findingArnFilters"]
            )
        )
    return out
