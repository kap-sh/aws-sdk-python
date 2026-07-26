"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#BucketInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.bucket_list


class BucketInfo(TypedDict, closed=True):
    buckets: NotRequired["capo_cloudsearch_domain.types.bucket_list.BucketList"]
    """<p>A list of the calculated facet values and counts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketInfo) -> dict:
    out: dict = {}
    if "buckets" in value:
        import capo_cloudsearch_domain.types.bucket_list

        out["buckets"] = capo_cloudsearch_domain.types.bucket_list.serialize_json(
            value["buckets"]
        )
    return out


def deserialize_json(data: dict) -> BucketInfo:
    out: BucketInfo = {}  # type: ignore[typeddict-item]
    if "buckets" in data:
        import capo_cloudsearch_domain.types.bucket_list

        out["buckets"] = capo_cloudsearch_domain.types.bucket_list.deserialize_json(
            data["buckets"]
        )
    return out
