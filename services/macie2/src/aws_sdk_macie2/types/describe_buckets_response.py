"""Generated from Smithy shape ``com.amazonaws.macie2#DescribeBucketsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_bucket_metadata
    import aws_sdk_macie2.types.__string


class DescribeBucketsResponse(TypedDict):
    buckets: NotRequired[
        "aws_sdk_macie2.types.__list_of_bucket_metadata.__listOfBucketMetadata"
    ]
    """<p>An array of objects, one for each bucket that matches the filter criteria specified in the request.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBucketsResponse) -> dict:
    out: dict = {}
    if "buckets" in value:
        import aws_sdk_macie2.types.__list_of_bucket_metadata

        out["buckets"] = aws_sdk_macie2.types.__list_of_bucket_metadata.serialize_json(
            value["buckets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeBucketsResponse:
    out: DescribeBucketsResponse = {}  # type: ignore[typeddict-item]
    if "buckets" in data:
        import aws_sdk_macie2.types.__list_of_bucket_metadata

        out["buckets"] = (
            aws_sdk_macie2.types.__list_of_bucket_metadata.deserialize_json(
                data["buckets"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
