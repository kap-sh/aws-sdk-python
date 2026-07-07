"""Generated from Smithy shape ``com.amazonaws.macie2#S3ClassificationScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.s3_classification_scope_exclusion


class S3ClassificationScope(TypedDict, closed=True):
    excludes: NotRequired[
        "aws_sdk_macie2.types.s3_classification_scope_exclusion.S3ClassificationScopeExclusion"
    ]
    """<p>The S3 buckets that are excluded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ClassificationScope) -> dict:
    out: dict = {}
    if "excludes" in value:
        import aws_sdk_macie2.types.s3_classification_scope_exclusion

        out["excludes"] = (
            aws_sdk_macie2.types.s3_classification_scope_exclusion.serialize_json(
                value["excludes"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3ClassificationScope:
    out: S3ClassificationScope = {}  # type: ignore[typeddict-item]
    if "excludes" in data:
        import aws_sdk_macie2.types.s3_classification_scope_exclusion

        out["excludes"] = (
            aws_sdk_macie2.types.s3_classification_scope_exclusion.deserialize_json(
                data["excludes"]
            )
        )
    return out
