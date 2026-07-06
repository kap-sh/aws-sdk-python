"""Generated from Smithy shape ``com.amazonaws.macie2#S3BucketDefinitionForJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of__string
    import aws_sdk_macie2.types.__string


class S3BucketDefinitionForJob(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account that owns the buckets.</p>"""
    buckets: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists the names of the buckets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketDefinitionForJob) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "buckets" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["buckets"] = aws_sdk_macie2.types.__list_of__string.serialize_json(
            value["buckets"]
        )
    return out


def deserialize_json(data: dict) -> S3BucketDefinitionForJob:
    out: S3BucketDefinitionForJob = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "buckets" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["buckets"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["buckets"]
        )
    return out
