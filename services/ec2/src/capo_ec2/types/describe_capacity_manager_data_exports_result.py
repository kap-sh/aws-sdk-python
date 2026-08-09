"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityManagerDataExportsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_data_export_response_set
    import capo_ec2.types.string


class DescribeCapacityManagerDataExportsResult(TypedDict, closed=True):
    capacity_manager_data_exports: NotRequired[
        "capo_ec2.types.capacity_manager_data_export_response_set.CapacityManagerDataExportResponseSet"
    ]
    """<p> Information about the data export configurations, including export settings, delivery status, and recent activity. </p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p> The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityManagerDataExportsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_manager_data_exports" in value:
        import capo_ec2.types.capacity_manager_data_export_response_set

        capo_ec2.types.capacity_manager_data_export_response_set.serialize_ec2_query(
            value["capacity_manager_data_exports"],
            pairs,
            f"{key_prefix}CapacityManagerDataExportSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCapacityManagerDataExportsResult:
    out: DescribeCapacityManagerDataExportsResult = {}  # type: ignore[typeddict-item]
    child_capacity_manager_data_exports = el.find("capacityManagerDataExportSet")
    if child_capacity_manager_data_exports is not None:
        import capo_ec2.types.capacity_manager_data_export_response_set

        out["capacity_manager_data_exports"] = (
            capo_ec2.types.capacity_manager_data_export_response_set.deserialize_ec2_query(
                child_capacity_manager_data_exports
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
