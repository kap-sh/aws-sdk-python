"""Generated from Smithy shape ``com.amazonaws.ec2#StartDeclarativePoliciesReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class StartDeclarativePoliciesReportRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    s3_bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the S3 bucket where the report will be saved. The bucket must be in the same Region where the report generation request is made.</p>"""
    s3_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix for your S3 object.</p>"""
    target_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The root ID, organizational unit ID, or account ID.</p> <p>Format:</p> <ul> <li> <p>For root: <code>r-ab12</code> </p> </li> <li> <p>For OU: <code>ou-ab12-cdef1234</code> </p> </li> <li> <p>For account: <code>123456789012</code> </p> </li> </ul>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StartDeclarativePoliciesReportRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "s3_bucket" in value:
        pairs.append((f"{prefix}.S3Bucket", str(value["s3_bucket"])))
    if "s3_prefix" in value:
        pairs.append((f"{prefix}.S3Prefix", str(value["s3_prefix"])))
    if "target_id" in value:
        pairs.append((f"{prefix}.TargetId", str(value["target_id"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> StartDeclarativePoliciesReportRequest:
    out: StartDeclarativePoliciesReportRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_s3_bucket = el.find("S3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    child_s3_prefix = el.find("S3Prefix")
    if child_s3_prefix is not None:
        out["s3_prefix"] = str(child_s3_prefix.text or "")
    child_target_id = el.find("TargetId")
    if child_target_id is not None:
        out["target_id"] = str(child_target_id.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
