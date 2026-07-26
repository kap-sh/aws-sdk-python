"""Generated from Smithy shape ``com.amazonaws.macie2#S3ClassificationScopeExclusionUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_s3_bucket_name
    import capo_macie2.types.classification_scope_update_operation


class S3ClassificationScopeExclusionUpdate(TypedDict, closed=True):
    bucket_names: NotRequired[
        "capo_macie2.types.__list_of_s3_bucket_name.__listOfS3BucketName"
    ]
    """<p>Depending on the value specified for the update operation (ClassificationScopeUpdateOperation), an array of strings that: lists the names of buckets to add or remove from the list, or specifies a new set of bucket names that overwrites all existing names in the list. Each string must be the full name of an existing S3 bucket. Values are case sensitive.</p>"""
    operation: NotRequired[
        "capo_macie2.types.classification_scope_update_operation.ClassificationScopeUpdateOperation"
    ]
    """<p>Specifies how to apply the changes to the exclusion list. Valid values are:</p> <ul><li><p>ADD - Append the specified bucket names to the current list.</p></li> <li><p>REMOVE - Remove the specified bucket names from the current list.</p></li> <li><p>REPLACE - Overwrite the current list with the specified list of bucket names. If you specify this value, Amazon Macie removes all existing names from the list and adds all the specified names to the list.</p></li></ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ClassificationScopeExclusionUpdate) -> dict:
    out: dict = {}
    if "bucket_names" in value:
        import capo_macie2.types.__list_of_s3_bucket_name

        out["bucketNames"] = capo_macie2.types.__list_of_s3_bucket_name.serialize_json(
            value["bucket_names"]
        )
    if "operation" in value:
        import capo_macie2.types.classification_scope_update_operation

        out["operation"] = (
            capo_macie2.types.classification_scope_update_operation.serialize_json(
                value["operation"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3ClassificationScopeExclusionUpdate:
    out: S3ClassificationScopeExclusionUpdate = {}  # type: ignore[typeddict-item]
    if "bucketNames" in data:
        import capo_macie2.types.__list_of_s3_bucket_name

        out["bucket_names"] = (
            capo_macie2.types.__list_of_s3_bucket_name.deserialize_json(
                data["bucketNames"]
            )
        )
    if "operation" in data:
        import capo_macie2.types.classification_scope_update_operation

        out["operation"] = (
            capo_macie2.types.classification_scope_update_operation.deserialize_json(
                data["operation"]
            )
        )
    return out
