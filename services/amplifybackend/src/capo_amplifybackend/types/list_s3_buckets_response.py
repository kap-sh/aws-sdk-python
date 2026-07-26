"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListS3BucketsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.list_of_s3_bucket_info


class ListS3BucketsResponse(TypedDict, closed=True):
    buckets: NotRequired[
        "capo_amplifybackend.types.list_of_s3_bucket_info.ListOfS3BucketInfo"
    ]
    """<p>The list of S3 buckets.</p>"""
    next_token: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>Reserved for future use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListS3BucketsResponse) -> dict:
    out: dict = {}
    if "buckets" in value:
        import capo_amplifybackend.types.list_of_s3_bucket_info

        out["buckets"] = (
            capo_amplifybackend.types.list_of_s3_bucket_info.serialize_json(
                value["buckets"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListS3BucketsResponse:
    out: ListS3BucketsResponse = {}  # type: ignore[typeddict-item]
    if "buckets" in data:
        import capo_amplifybackend.types.list_of_s3_bucket_info

        out["buckets"] = (
            capo_amplifybackend.types.list_of_s3_bucket_info.deserialize_json(
                data["buckets"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
