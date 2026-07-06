"""Generated from Smithy shape ``com.amazonaws.batch#ShareAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.float
    import aws_sdk_batch.types.string


class ShareAttributes(TypedDict, closed=True):
    share_identifier: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A share identifier or share identifier prefix. If the string ends with an asterisk (*), this entry specifies the weight factor to use for share identifiers that start with that prefix. The list of share identifiers in a fair-share policy can't overlap. For example, you can't have one that specifies a <code>shareIdentifier</code> of <code>UserA*</code> and another that specifies a <code>shareIdentifier</code> of <code>UserA1</code>.</p> <p>There can be no more than 500 share identifiers active in a job queue.</p> <p>The string is limited to 255 alphanumeric characters, and can be followed by an asterisk (*).</p>"""
    weight_factor: NotRequired["aws_sdk_batch.types.float.Float"]
    """<p>The weight factor for the share identifier. The default value is 1.0. A lower value has a higher priority for compute resources. For example, jobs that use a share identifier with a weight factor of 0.125 (1/8) get 8 times the compute resources of jobs that use a share identifier with a weight factor of 1.</p> <p>The smallest supported value is 0.0001, and the largest supported value is 999.9999.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShareAttributes) -> dict:
    out: dict = {}
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "weight_factor" in value:
        out["weightFactor"] = value["weight_factor"]
    return out


def deserialize_json(data: dict) -> ShareAttributes:
    out: ShareAttributes = {}  # type: ignore[typeddict-item]
    if "shareIdentifier" in data:
        out["share_identifier"] = data["shareIdentifier"]
    if "weightFactor" in data:
        out["weight_factor"] = data["weightFactor"]
    return out
