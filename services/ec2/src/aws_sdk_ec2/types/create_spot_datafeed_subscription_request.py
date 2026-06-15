"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSpotDatafeedSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class CreateSpotDatafeedSubscriptionRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<p>The name of the Amazon S3 bucket in which to store the Spot Instance data feed. For more information about bucket names, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html\">Bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix for the data feed file names.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSpotDatafeedSubscriptionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "bucket" in value:
        pairs.append((f"{prefix}.Bucket", str(value["bucket"])))
    if "prefix" in value:
        pairs.append((f"{prefix}.Prefix", str(value["prefix"])))


def deserialize_ec2_query(el: Element) -> CreateSpotDatafeedSubscriptionRequest:
    out: CreateSpotDatafeedSubscriptionRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    return out
