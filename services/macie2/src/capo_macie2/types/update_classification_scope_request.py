"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateClassificationScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.s3_classification_scope_update


class UpdateClassificationScopeRequest(TypedDict, closed=True):
    id: "capo_macie2.types.__string.__string"
    """<p>The unique identifier for the Amazon Macie resource that the request applies to.</p>"""
    s3: NotRequired[
        "capo_macie2.types.s3_classification_scope_update.S3ClassificationScopeUpdate"
    ]
    """<p>The S3 buckets to add or remove from the exclusion list defined by the classification scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClassificationScopeRequest) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_macie2.types.s3_classification_scope_update

        out["s3"] = capo_macie2.types.s3_classification_scope_update.serialize_json(
            value["s3"]
        )
    return out


def deserialize_json(data: dict) -> UpdateClassificationScopeRequest:
    out: UpdateClassificationScopeRequest = {}  # type: ignore[typeddict-item]
    if "s3" in data:
        import capo_macie2.types.s3_classification_scope_update

        out["s3"] = capo_macie2.types.s3_classification_scope_update.deserialize_json(
            data["s3"]
        )
    return out
