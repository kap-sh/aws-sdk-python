"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScanConfigurationsFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_scan_configuration_arn_filter_list
    import capo_inspector2.types.cis_scan_name_filter_list
    import capo_inspector2.types.resource_tag_filter_list


class ListCisScanConfigurationsFilterCriteria(TypedDict, closed=True):
    scan_name_filters: NotRequired[
        "capo_inspector2.types.cis_scan_name_filter_list.CisScanNameFilterList"
    ]
    """<p>The list of scan name filters.</p>"""
    target_resource_tag_filters: NotRequired[
        "capo_inspector2.types.resource_tag_filter_list.ResourceTagFilterList"
    ]
    """<p>The list of target resource tag filters.</p>"""
    scan_configuration_arn_filters: NotRequired[
        "capo_inspector2.types.cis_scan_configuration_arn_filter_list.CisScanConfigurationArnFilterList"
    ]
    """<p>The list of scan configuration ARN filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScanConfigurationsFilterCriteria) -> dict:
    out: dict = {}
    if "scan_name_filters" in value:
        import capo_inspector2.types.cis_scan_name_filter_list

        out["scanNameFilters"] = (
            capo_inspector2.types.cis_scan_name_filter_list.serialize_json(
                value["scan_name_filters"]
            )
        )
    if "target_resource_tag_filters" in value:
        import capo_inspector2.types.resource_tag_filter_list

        out["targetResourceTagFilters"] = (
            capo_inspector2.types.resource_tag_filter_list.serialize_json(
                value["target_resource_tag_filters"]
            )
        )
    if "scan_configuration_arn_filters" in value:
        import capo_inspector2.types.cis_scan_configuration_arn_filter_list

        out["scanConfigurationArnFilters"] = (
            capo_inspector2.types.cis_scan_configuration_arn_filter_list.serialize_json(
                value["scan_configuration_arn_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCisScanConfigurationsFilterCriteria:
    out: ListCisScanConfigurationsFilterCriteria = {}  # type: ignore[typeddict-item]
    if "scanNameFilters" in data:
        import capo_inspector2.types.cis_scan_name_filter_list

        out["scan_name_filters"] = (
            capo_inspector2.types.cis_scan_name_filter_list.deserialize_json(
                data["scanNameFilters"]
            )
        )
    if "targetResourceTagFilters" in data:
        import capo_inspector2.types.resource_tag_filter_list

        out["target_resource_tag_filters"] = (
            capo_inspector2.types.resource_tag_filter_list.deserialize_json(
                data["targetResourceTagFilters"]
            )
        )
    if "scanConfigurationArnFilters" in data:
        import capo_inspector2.types.cis_scan_configuration_arn_filter_list

        out["scan_configuration_arn_filters"] = (
            capo_inspector2.types.cis_scan_configuration_arn_filter_list.deserialize_json(
                data["scanConfigurationArnFilters"]
            )
        )
    return out
