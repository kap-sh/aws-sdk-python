"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisFactor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string


class ContributionAnalysisFactor(TypedDict, closed=True):
    field_name: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The field name of the <code>ContributionAnalysisFactor</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContributionAnalysisFactor) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    return out


def deserialize_json(data: dict) -> ContributionAnalysisFactor:
    out: ContributionAnalysisFactor = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    return out
