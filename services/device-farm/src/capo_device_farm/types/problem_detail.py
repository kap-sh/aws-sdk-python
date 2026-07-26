"""Generated from Smithy shape ``com.amazonaws.devicefarm#ProblemDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.name


class ProblemDetail(TypedDict, closed=True):
    arn: NotRequired["capo_device_farm.types.amazon_resource_name.AmazonResourceName"]
    """<p>The problem detail's ARN.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The problem detail's name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProblemDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProblemDetail:
    out: ProblemDetail = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    return out
