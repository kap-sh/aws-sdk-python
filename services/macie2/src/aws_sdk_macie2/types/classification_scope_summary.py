"""Generated from Smithy shape ``com.amazonaws.macie2#ClassificationScopeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.classification_scope_id
    import aws_sdk_macie2.types.classification_scope_name


class ClassificationScopeSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_macie2.types.classification_scope_id.ClassificationScopeId"
    ]
    """<p>The unique identifier for the classification scope.</p>"""
    name: NotRequired[
        "aws_sdk_macie2.types.classification_scope_name.ClassificationScopeName"
    ]
    """<p>The name of the classification scope: automated-sensitive-data-discovery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClassificationScopeSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ClassificationScopeSummary:
    out: ClassificationScopeSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    return out
