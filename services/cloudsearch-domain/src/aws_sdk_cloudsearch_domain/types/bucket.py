"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Bucket``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.long
    import aws_sdk_cloudsearch_domain.types.string


class Bucket(TypedDict, closed=True):
    value: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    """<p>The facet value being counted.</p>"""
    count: "aws_sdk_cloudsearch_domain.types.long.Long"
    """<p>The number of hits that contain the facet value in the specified facet field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Bucket) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    out["count"] = value.get("count", 0)
    return out


def deserialize_json(data: dict) -> Bucket:
    out: Bucket = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "count" in data:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
