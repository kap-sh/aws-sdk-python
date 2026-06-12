"""Generated from Smithy shape ``com.amazonaws.glue#UpdateDataQualityRulesetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_ruleset_string
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.name_string


class UpdateDataQualityRulesetRequest(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the data quality ruleset.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the ruleset.</p>"""
    ruleset: NotRequired[
        "aws_sdk_glue.types.data_quality_ruleset_string.DataQualityRulesetString"
    ]
    """<p>A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDataQualityRulesetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "ruleset" in value:
        out["Ruleset"] = value["ruleset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDataQualityRulesetRequest:
    out: UpdateDataQualityRulesetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDataQualityRulesetRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Ruleset" in data:
        out["ruleset"] = data["Ruleset"]
    return out
