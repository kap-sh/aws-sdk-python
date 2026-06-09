"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityManagerDataExportsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_data_export_response_set
    import aws_sdk_ec2.types.string


class DescribeCapacityManagerDataExportsResult(TypedDict):
    capacity_manager_data_exports: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_data_export_response_set.CapacityManagerDataExportResponseSet"
    ]
    """<p> Information about the data export configurations, including export settings, delivery status, and recent activity. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityManagerDataExportsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_manager_data_exports" in value:
        import aws_sdk_ec2.types.capacity_manager_data_export_response_set

        aws_sdk_ec2.types.capacity_manager_data_export_response_set.serialize_ec2_query(
            value["capacity_manager_data_exports"],
            pairs,
            f"{prefix}.CapacityManagerDataExportSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCapacityManagerDataExportsResult:
    out: DescribeCapacityManagerDataExportsResult = {}  # type: ignore[typeddict-item]
    if el.find("CapacityManagerDataExportSet") is not None:
        import aws_sdk_ec2.types.capacity_manager_data_export_response_set

        out["capacity_manager_data_exports"] = (
            aws_sdk_ec2.types.capacity_manager_data_export_response_set.deserialize_ec2_query(
                el, "CapacityManagerDataExportSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
