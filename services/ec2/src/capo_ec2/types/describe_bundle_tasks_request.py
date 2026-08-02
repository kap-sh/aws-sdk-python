"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeBundleTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.bundle_id_string_list
    import capo_ec2.types.filter_list


class DescribeBundleTasksRequest(TypedDict, closed=True):
    bundle_ids: NotRequired["capo_ec2.types.bundle_id_string_list.BundleIdStringList"]
    """<p>The bundle task IDs.</p> <p>Default: Describes all your bundle tasks.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>bundle-id</code> - The ID of the bundle task.</p> </li> <li> <p> <code>error-code</code> - If the task failed, the error code returned.</p> </li> <li> <p> <code>error-message</code> - If the task failed, the error message returned.</p> </li> <li> <p> <code>instance-id</code> - The ID of the instance.</p> </li> <li> <p> <code>progress</code> - The level of task completion, as a percentage (for example, 20%).</p> </li> <li> <p> <code>s3-bucket</code> - The Amazon S3 bucket to store the AMI.</p> </li> <li> <p> <code>s3-prefix</code> - The beginning of the AMI name.</p> </li> <li> <p> <code>start-time</code> - The time the task started (for example, 2013-09-15T17:15:20.000Z).</p> </li> <li> <p> <code>state</code> - The state of the task (<code>pending</code> | <code>waiting-for-shutdown</code> | <code>bundling</code> | <code>storing</code> | <code>cancelling</code> | <code>complete</code> | <code>failed</code>).</p> </li> <li> <p> <code>update-time</code> - The time of the most recent update for the task.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeBundleTasksRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "bundle_ids" in value:
        import capo_ec2.types.bundle_id_string_list

        capo_ec2.types.bundle_id_string_list.serialize_ec2_query(
            value["bundle_ids"], pairs, f"{key_prefix}BundleIds"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )


def deserialize_ec2_query(el: Element) -> DescribeBundleTasksRequest:
    out: DescribeBundleTasksRequest = {}  # type: ignore[typeddict-item]
    if el.find("BundleIds") is not None:
        import capo_ec2.types.bundle_id_string_list

        out["bundle_ids"] = capo_ec2.types.bundle_id_string_list.deserialize_ec2_query(
            el, "BundleIds"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filters")
    return out
