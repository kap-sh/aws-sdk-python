"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#BucketInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.bucket_list


class BucketInfo(TypedDict):
    buckets: NotRequired["aws_sdk_cloudsearch_domain.types.bucket_list.BucketList"]
    """<p>A list of the calculated facet values and counts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketInfo) -> dict:
    out: dict = {}
    if "buckets" in value:
        import aws_sdk_cloudsearch_domain.types.bucket_list

        out["buckets"] = aws_sdk_cloudsearch_domain.types.bucket_list.serialize_json(
            value["buckets"]
        )
    return out


def deserialize_json(data: dict) -> BucketInfo:
    out: BucketInfo = {}  # type: ignore[typeddict-item]
    if "buckets" in data:
        import aws_sdk_cloudsearch_domain.types.bucket_list

        out["buckets"] = aws_sdk_cloudsearch_domain.types.bucket_list.deserialize_json(
            data["buckets"]
        )
    return out
