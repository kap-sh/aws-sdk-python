"""Generated from Smithy shape ``com.amazonaws.guardduty#ResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.instance_arn


class ResourceDetails(TypedDict, closed=True):
    instance_arn: NotRequired["aws_sdk_guardduty.types.instance_arn.InstanceArn"]
    """<p>Instance ARN that was scanned in the scan entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDetails) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    return out


def deserialize_json(data: dict) -> ResourceDetails:
    out: ResourceDetails = {}  # type: ignore[typeddict-item]
    if "instanceArn" in data:
        out["instance_arn"] = data["instanceArn"]
    return out
