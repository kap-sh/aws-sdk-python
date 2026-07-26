"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeRedshiftIdcApplicationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string


class DescribeRedshiftIdcApplicationsMessage(TypedDict, closed=True):
    redshift_idc_application_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeRedshiftIdcApplicationsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "redshift_idc_application_arn" in value:
        pairs.append(
            (
                f"{prefix}.RedshiftIdcApplicationArn",
                str(value["redshift_idc_application_arn"]),
            )
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeRedshiftIdcApplicationsMessage:
    out: DescribeRedshiftIdcApplicationsMessage = {}  # type: ignore[typeddict-item]
    child_redshift_idc_application_arn = el.find("RedshiftIdcApplicationArn")
    if child_redshift_idc_application_arn is not None:
        out["redshift_idc_application_arn"] = str(
            child_redshift_idc_application_arn.text or ""
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
