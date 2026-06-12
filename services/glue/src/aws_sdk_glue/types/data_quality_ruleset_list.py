"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRulesetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_ruleset_list_details

DataQualityRulesetList: TypeAlias = list[
    "aws_sdk_glue.types.data_quality_ruleset_list_details.DataQualityRulesetListDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRulesetList) -> list:
    import aws_sdk_glue.types.data_quality_ruleset_list_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.data_quality_ruleset_list_details.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityRulesetList:
    import aws_sdk_glue.types.data_quality_ruleset_list_details

    out: DataQualityRulesetList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.data_quality_ruleset_list_details.deserialize_aws_json_1_1(
                item
            )
        )
    return out
