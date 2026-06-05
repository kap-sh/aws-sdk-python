"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceEventWindowRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_event_window_cron_expression
    import aws_sdk_ec2.types.instance_event_window_time_range_request_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateInstanceEventWindowRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the event window.</p>"""
    time_ranges: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_time_range_request_set.InstanceEventWindowTimeRangeRequestSet"
    ]
    """<p>The time range for the event window. If you specify a time range, you can't specify a cron expression.</p>"""
    cron_expression: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_cron_expression.InstanceEventWindowCronExpression"
    ]
    """<p>The cron expression for the event window, for example, <code>* 0-4,20-23 * * 1,5</code>. If you specify a cron expression, you can't specify a time range.</p> <p>Constraints:</p> <ul> <li> <p>Only hour and day of the week values are supported.</p> </li> <li> <p>For day of the week values, you can specify either integers <code>0</code> through <code>6</code>, or alternative single values <code>SUN</code> through <code>SAT</code>.</p> </li> <li> <p>The minute, month, and year must be specified by <code>*</code>.</p> </li> <li> <p>The hour value must be one or a multiple range, for example, <code>0-4</code> or <code>0-4,20-23</code>.</p> </li> <li> <p>Each hour range must be >= 2 hours, for example, <code>0-2</code> or <code>20-23</code>.</p> </li> <li> <p>The event window must be >= 4 hours. The combined total time ranges in the event window must be >= 4 hours.</p> </li> </ul> <p>For more information about cron expressions, see <a href=\"https://en.wikipedia.org/wiki/Cron\">cron</a> on the <i>Wikipedia website</i>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateInstanceEventWindowRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "time_ranges" in value:
        import aws_sdk_ec2.types.instance_event_window_time_range_request_set

        aws_sdk_ec2.types.instance_event_window_time_range_request_set.serialize_ec2_query(
            value["time_ranges"], pairs, f"{prefix}.TimeRanges"
        )
    if "cron_expression" in value:
        pairs.append((f"{prefix}.CronExpression", str(value["cron_expression"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> CreateInstanceEventWindowRequest:
    out: CreateInstanceEventWindowRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    if el.find("TimeRanges") is not None:
        import aws_sdk_ec2.types.instance_event_window_time_range_request_set

        out["time_ranges"] = (
            aws_sdk_ec2.types.instance_event_window_time_range_request_set.deserialize_ec2_query(
                el, "TimeRanges"
            )
        )
    child_cron_expression = el.find("CronExpression")
    if child_cron_expression is not None:
        out["cron_expression"] = str(child_cron_expression.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
