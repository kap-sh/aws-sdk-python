"""Generated from Smithy shape ``com.amazonaws.redshift#TableRestoreStatusMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.table_restore_status_list


class TableRestoreStatusMessage(TypedDict, closed=True):
    table_restore_status_details: NotRequired[
        "aws_sdk_redshift.types.table_restore_status_list.TableRestoreStatusList"
    ]
    """<p>A list of status details for one or more table restore requests.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A pagination token that can be used in a subsequent <a>DescribeTableRestoreStatus</a> request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TableRestoreStatusMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "table_restore_status_details" in value:
        import aws_sdk_redshift.types.table_restore_status_list

        aws_sdk_redshift.types.table_restore_status_list.serialize_query(
            value["table_restore_status_details"],
            pairs,
            f"{prefix}.TableRestoreStatusDetails",
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> TableRestoreStatusMessage:
    out: TableRestoreStatusMessage = {}  # type: ignore[typeddict-item]
    child_table_restore_status_details = el.find("TableRestoreStatusDetails")
    if child_table_restore_status_details is not None:
        import aws_sdk_redshift.types.table_restore_status_list

        out["table_restore_status_details"] = (
            aws_sdk_redshift.types.table_restore_status_list.deserialize_query(
                child_table_restore_status_details
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
