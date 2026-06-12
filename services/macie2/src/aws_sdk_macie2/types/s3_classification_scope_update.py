"""Generated from Smithy shape ``com.amazonaws.macie2#S3ClassificationScopeUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.s3_classification_scope_exclusion_update


class S3ClassificationScopeUpdate(TypedDict):
    excludes: NotRequired[
        "aws_sdk_macie2.types.s3_classification_scope_exclusion_update.S3ClassificationScopeExclusionUpdate"
    ]
    """<p>The names of the S3 buckets to add or remove from the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ClassificationScopeUpdate) -> dict:
    out: dict = {}
    if "excludes" in value:
        import aws_sdk_macie2.types.s3_classification_scope_exclusion_update

        out["excludes"] = (
            aws_sdk_macie2.types.s3_classification_scope_exclusion_update.serialize_json(
                value["excludes"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3ClassificationScopeUpdate:
    out: S3ClassificationScopeUpdate = {}  # type: ignore[typeddict-item]
    if "excludes" in data:
        import aws_sdk_macie2.types.s3_classification_scope_exclusion_update

        out["excludes"] = (
            aws_sdk_macie2.types.s3_classification_scope_exclusion_update.deserialize_json(
                data["excludes"]
            )
        )
    return out
