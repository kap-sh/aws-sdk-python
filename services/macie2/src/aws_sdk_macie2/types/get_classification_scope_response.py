"""Generated from Smithy shape ``com.amazonaws.macie2#GetClassificationScopeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.classification_scope_id
    import aws_sdk_macie2.types.classification_scope_name
    import aws_sdk_macie2.types.s3_classification_scope


class GetClassificationScopeResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_macie2.types.classification_scope_id.ClassificationScopeId"
    ]
    """<p>The unique identifier for the classification scope.</p>"""
    name: NotRequired[
        "aws_sdk_macie2.types.classification_scope_name.ClassificationScopeName"
    ]
    """<p>The name of the classification scope: automated-sensitive-data-discovery.</p>"""
    s3: NotRequired[
        "aws_sdk_macie2.types.s3_classification_scope.S3ClassificationScope"
    ]
    """<p>The S3 buckets that are excluded from automated sensitive data discovery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClassificationScopeResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "s3" in value:
        import aws_sdk_macie2.types.s3_classification_scope

        out["s3"] = aws_sdk_macie2.types.s3_classification_scope.serialize_json(
            value["s3"]
        )
    return out


def deserialize_json(data: dict) -> GetClassificationScopeResponse:
    out: GetClassificationScopeResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "s3" in data:
        import aws_sdk_macie2.types.s3_classification_scope

        out["s3"] = aws_sdk_macie2.types.s3_classification_scope.deserialize_json(
            data["s3"]
        )
    return out
