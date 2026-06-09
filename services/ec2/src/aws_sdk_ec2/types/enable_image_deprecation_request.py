"""Generated from Smithy shape ``com.amazonaws.ec2#EnableImageDeprecationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.millisecond_date_time


class EnableImageDeprecationRequest(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    deprecate_at: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time to deprecate the AMI, in UTC, in the following format: <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z. If you specify a value for seconds, Amazon EC2 rounds the seconds to the nearest minute.</p> <p>You can’t specify a date in the past. The upper limit for <code>DeprecateAt</code> is 10 years from now, except for public AMIs, where the upper limit is 2 years from the creation date.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableImageDeprecationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "deprecate_at" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["deprecate_at"], pairs, f"{prefix}.DeprecateAt"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> EnableImageDeprecationRequest:
    out: EnableImageDeprecationRequest = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_deprecate_at = el.find("DeprecateAt")
    if child_deprecate_at is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["deprecate_at"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_deprecate_at
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
