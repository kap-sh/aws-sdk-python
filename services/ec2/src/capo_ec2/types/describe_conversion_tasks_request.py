"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeConversionTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.conversion_id_string_list


class DescribeConversionTasksRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    conversion_task_ids: NotRequired[
        "capo_ec2.types.conversion_id_string_list.ConversionIdStringList"
    ]
    """<p>The conversion task IDs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeConversionTasksRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "conversion_task_ids" in value:
        import capo_ec2.types.conversion_id_string_list

        capo_ec2.types.conversion_id_string_list.serialize_ec2_query(
            value["conversion_task_ids"], pairs, f"{key_prefix}ConversionTaskId"
        )


def deserialize_ec2_query(el: Element) -> DescribeConversionTasksRequest:
    out: DescribeConversionTasksRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_conversion_task_ids = el.find("conversionTaskId")
    if child_conversion_task_ids is not None:
        import capo_ec2.types.conversion_id_string_list

        out["conversion_task_ids"] = (
            capo_ec2.types.conversion_id_string_list.deserialize_ec2_query(
                child_conversion_task_ids
            )
        )
    return out
