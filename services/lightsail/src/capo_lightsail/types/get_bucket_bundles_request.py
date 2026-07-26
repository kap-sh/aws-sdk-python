"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBucketBundlesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean


class GetBucketBundlesRequest(TypedDict, closed=True):
    include_inactive: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether to include inactive (unavailable) bundles in the response of your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBucketBundlesRequest) -> dict:
    out: dict = {}
    if "include_inactive" in value:
        out["includeInactive"] = value["include_inactive"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBucketBundlesRequest:
    out: GetBucketBundlesRequest = {}  # type: ignore[typeddict-item]
    if "includeInactive" in data:
        out["include_inactive"] = data["includeInactive"]
    return out
