"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScansFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id_filter_list
    import aws_sdk_inspector2.types.cis_number_filter_list
    import aws_sdk_inspector2.types.cis_scan_arn_filter_list
    import aws_sdk_inspector2.types.cis_scan_configuration_arn_filter_list
    import aws_sdk_inspector2.types.cis_scan_date_filter_list
    import aws_sdk_inspector2.types.cis_scan_name_filter_list
    import aws_sdk_inspector2.types.cis_scan_status_filter_list
    import aws_sdk_inspector2.types.cis_scheduled_by_filter_list
    import aws_sdk_inspector2.types.resource_id_filter_list
    import aws_sdk_inspector2.types.resource_tag_filter_list


class ListCisScansFilterCriteria(TypedDict, closed=True):
    scan_name_filters: NotRequired[
        "aws_sdk_inspector2.types.cis_scan_name_filter_list.CisScanNameFilterList"
    ]
    """<p>The list of scan name filters.</p>"""
    target_resource_tag_filters: NotRequired[
        "aws_sdk_inspector2.types.resource_tag_filter_list.ResourceTagFilterList"
    ]
    """<p>The list of target resource tag filters.</p>"""
    target_resource_id_filters: NotRequired[
        "aws_sdk_inspector2.types.resource_id_filter_list.ResourceIdFilterList"
    ]
    """<p>The list of target resource ID filters.</p>"""
    scan_status_filters: NotRequired[
        "aws_sdk_inspector2.types.cis_scan_status_filter_list.CisScanStatusFilterList"
    ]
    """<p>The list of scan status filters.</p>"""
    scan_at_filters: NotRequired[
        "aws_sdk_inspector2.types.cis_scan_date_filter_list.CisScanDateFilterList"
    ]
    """<p>The list of scan at filters.</p>"""
    scan_configuration_arn_filters: NotRequired[
        "aws_sdk_inspector2.types.cis_scan_configuration_arn_filter_list.CisScanConfigurationArnFilterList"
    ]
    """<p>The list of scan configuration ARN filters.</p>"""
    scan_arn_filters: NotRequired[
        "aws_sdk_inspector2.types.cis_scan_arn_filter_list.CisScanArnFilterList"
    ]
    """<p>The list of scan ARN filters.</p>"""
    scheduled_by_filters: NotRequired[
        "aws_sdk_inspector2.types.cis_scheduled_by_filter_list.CisScheduledByFilterList"
    ]
    """<p>The list of scheduled by filters.</p>"""
    failed_checks_filters: NotRequired[
        "aws_sdk_inspector2.types.cis_number_filter_list.CisNumberFilterList"
    ]
    """<p>The list of failed checks filters.</p>"""
    target_account_id_filters: NotRequired[
        "aws_sdk_inspector2.types.account_id_filter_list.AccountIdFilterList"
    ]
    """<p>The list of target account ID filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScansFilterCriteria) -> dict:
    out: dict = {}
    if "scan_name_filters" in value:
        import aws_sdk_inspector2.types.cis_scan_name_filter_list

        out["scanNameFilters"] = (
            aws_sdk_inspector2.types.cis_scan_name_filter_list.serialize_json(
                value["scan_name_filters"]
            )
        )
    if "target_resource_tag_filters" in value:
        import aws_sdk_inspector2.types.resource_tag_filter_list

        out["targetResourceTagFilters"] = (
            aws_sdk_inspector2.types.resource_tag_filter_list.serialize_json(
                value["target_resource_tag_filters"]
            )
        )
    if "target_resource_id_filters" in value:
        import aws_sdk_inspector2.types.resource_id_filter_list

        out["targetResourceIdFilters"] = (
            aws_sdk_inspector2.types.resource_id_filter_list.serialize_json(
                value["target_resource_id_filters"]
            )
        )
    if "scan_status_filters" in value:
        import aws_sdk_inspector2.types.cis_scan_status_filter_list

        out["scanStatusFilters"] = (
            aws_sdk_inspector2.types.cis_scan_status_filter_list.serialize_json(
                value["scan_status_filters"]
            )
        )
    if "scan_at_filters" in value:
        import aws_sdk_inspector2.types.cis_scan_date_filter_list

        out["scanAtFilters"] = (
            aws_sdk_inspector2.types.cis_scan_date_filter_list.serialize_json(
                value["scan_at_filters"]
            )
        )
    if "scan_configuration_arn_filters" in value:
        import aws_sdk_inspector2.types.cis_scan_configuration_arn_filter_list

        out["scanConfigurationArnFilters"] = (
            aws_sdk_inspector2.types.cis_scan_configuration_arn_filter_list.serialize_json(
                value["scan_configuration_arn_filters"]
            )
        )
    if "scan_arn_filters" in value:
        import aws_sdk_inspector2.types.cis_scan_arn_filter_list

        out["scanArnFilters"] = (
            aws_sdk_inspector2.types.cis_scan_arn_filter_list.serialize_json(
                value["scan_arn_filters"]
            )
        )
    if "scheduled_by_filters" in value:
        import aws_sdk_inspector2.types.cis_scheduled_by_filter_list

        out["scheduledByFilters"] = (
            aws_sdk_inspector2.types.cis_scheduled_by_filter_list.serialize_json(
                value["scheduled_by_filters"]
            )
        )
    if "failed_checks_filters" in value:
        import aws_sdk_inspector2.types.cis_number_filter_list

        out["failedChecksFilters"] = (
            aws_sdk_inspector2.types.cis_number_filter_list.serialize_json(
                value["failed_checks_filters"]
            )
        )
    if "target_account_id_filters" in value:
        import aws_sdk_inspector2.types.account_id_filter_list

        out["targetAccountIdFilters"] = (
            aws_sdk_inspector2.types.account_id_filter_list.serialize_json(
                value["target_account_id_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCisScansFilterCriteria:
    out: ListCisScansFilterCriteria = {}  # type: ignore[typeddict-item]
    if "scanNameFilters" in data:
        import aws_sdk_inspector2.types.cis_scan_name_filter_list

        out["scan_name_filters"] = (
            aws_sdk_inspector2.types.cis_scan_name_filter_list.deserialize_json(
                data["scanNameFilters"]
            )
        )
    if "targetResourceTagFilters" in data:
        import aws_sdk_inspector2.types.resource_tag_filter_list

        out["target_resource_tag_filters"] = (
            aws_sdk_inspector2.types.resource_tag_filter_list.deserialize_json(
                data["targetResourceTagFilters"]
            )
        )
    if "targetResourceIdFilters" in data:
        import aws_sdk_inspector2.types.resource_id_filter_list

        out["target_resource_id_filters"] = (
            aws_sdk_inspector2.types.resource_id_filter_list.deserialize_json(
                data["targetResourceIdFilters"]
            )
        )
    if "scanStatusFilters" in data:
        import aws_sdk_inspector2.types.cis_scan_status_filter_list

        out["scan_status_filters"] = (
            aws_sdk_inspector2.types.cis_scan_status_filter_list.deserialize_json(
                data["scanStatusFilters"]
            )
        )
    if "scanAtFilters" in data:
        import aws_sdk_inspector2.types.cis_scan_date_filter_list

        out["scan_at_filters"] = (
            aws_sdk_inspector2.types.cis_scan_date_filter_list.deserialize_json(
                data["scanAtFilters"]
            )
        )
    if "scanConfigurationArnFilters" in data:
        import aws_sdk_inspector2.types.cis_scan_configuration_arn_filter_list

        out["scan_configuration_arn_filters"] = (
            aws_sdk_inspector2.types.cis_scan_configuration_arn_filter_list.deserialize_json(
                data["scanConfigurationArnFilters"]
            )
        )
    if "scanArnFilters" in data:
        import aws_sdk_inspector2.types.cis_scan_arn_filter_list

        out["scan_arn_filters"] = (
            aws_sdk_inspector2.types.cis_scan_arn_filter_list.deserialize_json(
                data["scanArnFilters"]
            )
        )
    if "scheduledByFilters" in data:
        import aws_sdk_inspector2.types.cis_scheduled_by_filter_list

        out["scheduled_by_filters"] = (
            aws_sdk_inspector2.types.cis_scheduled_by_filter_list.deserialize_json(
                data["scheduledByFilters"]
            )
        )
    if "failedChecksFilters" in data:
        import aws_sdk_inspector2.types.cis_number_filter_list

        out["failed_checks_filters"] = (
            aws_sdk_inspector2.types.cis_number_filter_list.deserialize_json(
                data["failedChecksFilters"]
            )
        )
    if "targetAccountIdFilters" in data:
        import aws_sdk_inspector2.types.account_id_filter_list

        out["target_account_id_filters"] = (
            aws_sdk_inspector2.types.account_id_filter_list.deserialize_json(
                data["targetAccountIdFilters"]
            )
        )
    return out
