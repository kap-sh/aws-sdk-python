"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeRedshiftIdcApplicationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.redshift_idc_application_list
    import capo_redshift.types.string


class DescribeRedshiftIdcApplicationsResult(TypedDict, closed=True):
    redshift_idc_applications: NotRequired[
        "capo_redshift.types.redshift_idc_application_list.RedshiftIdcApplicationList"
    ]
    """<p>The list of Amazon Redshift IAM Identity Center applications.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeRedshiftIdcApplicationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "redshift_idc_applications" in value:
        import capo_redshift.types.redshift_idc_application_list

        capo_redshift.types.redshift_idc_application_list.serialize_query(
            value["redshift_idc_applications"],
            pairs,
            f"{key_prefix}RedshiftIdcApplications",
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeRedshiftIdcApplicationsResult:
    out: DescribeRedshiftIdcApplicationsResult = {}  # type: ignore[typeddict-item]
    child_redshift_idc_applications = el.find("RedshiftIdcApplications")
    if child_redshift_idc_applications is not None:
        import capo_redshift.types.redshift_idc_application_list

        out["redshift_idc_applications"] = (
            capo_redshift.types.redshift_idc_application_list.deserialize_query(
                child_redshift_idc_applications
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
