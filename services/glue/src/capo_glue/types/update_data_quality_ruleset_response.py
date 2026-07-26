"""Generated from Smithy shape ``com.amazonaws.glue#UpdateDataQualityRulesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_ruleset_string
    import capo_glue.types.description_string
    import capo_glue.types.name_string


class UpdateDataQualityRulesetResponse(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the data quality ruleset.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the ruleset.</p>"""
    ruleset: NotRequired[
        "capo_glue.types.data_quality_ruleset_string.DataQualityRulesetString"
    ]
    """<p>A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDataQualityRulesetResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "ruleset" in value:
        out["Ruleset"] = value["ruleset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDataQualityRulesetResponse:
    out: UpdateDataQualityRulesetResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Ruleset" in data:
        out["ruleset"] = data["Ruleset"]
    return out
