"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeConversionTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.conversion_id_string_list


class DescribeConversionTasksRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    conversion_task_ids: NotRequired[
        "aws_sdk_ec2.types.conversion_id_string_list.ConversionIdStringList"
    ]
    """<p>The conversion task IDs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeConversionTasksRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "conversion_task_ids" in value:
        import aws_sdk_ec2.types.conversion_id_string_list

        aws_sdk_ec2.types.conversion_id_string_list.serialize_ec2_query(
            value["conversion_task_ids"], pairs, f"{prefix}.ConversionTaskId"
        )


def deserialize_ec2_query(el: Element) -> DescribeConversionTasksRequest:
    out: DescribeConversionTasksRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("ConversionTaskId") is not None:
        import aws_sdk_ec2.types.conversion_id_string_list

        out["conversion_task_ids"] = (
            aws_sdk_ec2.types.conversion_id_string_list.deserialize_ec2_query(
                el, "ConversionTaskId"
            )
        )
    return out
