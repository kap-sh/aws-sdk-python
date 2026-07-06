"""Generated from Smithy shape ``com.amazonaws.omics#UpdateRunCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.cache_behavior
    import aws_sdk_omics.types.run_cache_id
    import aws_sdk_omics.types.user_custom_description
    import aws_sdk_omics.types.user_custom_name


class UpdateRunCacheRequest(TypedDict, closed=True):
    cache_behavior: NotRequired["aws_sdk_omics.types.cache_behavior.CacheBehavior"]
    """<p>Update the default run cache behavior.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.user_custom_description.UserCustomDescription"
    ]
    """<p>Update the run cache description.</p>"""
    id: "aws_sdk_omics.types.run_cache_id.RunCacheId"
    """<p>The identifier of the run cache you want to update.</p>"""
    name: NotRequired["aws_sdk_omics.types.user_custom_name.UserCustomName"]
    """<p>Update the name of the run cache.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRunCacheRequest) -> dict:
    out: dict = {}
    if "cache_behavior" in value:
        out["cacheBehavior"] = value["cache_behavior"]
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateRunCacheRequest:
    out: UpdateRunCacheRequest = {}  # type: ignore[typeddict-item]
    if "cacheBehavior" in data:
        out["cache_behavior"] = data["cacheBehavior"]
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    return out
