"""Generated from Smithy shape ``com.amazonaws.glue#CreateDataQualityRulesetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_ruleset_string
    import aws_sdk_glue.types.data_quality_target_table
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.tags_map


class CreateDataQualityRulesetRequest(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>A unique name for the data quality ruleset.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the data quality ruleset.</p>"""
    ruleset: "aws_sdk_glue.types.data_quality_ruleset_string.DataQualityRulesetString"
    """<p>A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>A list of tags applied to the data quality ruleset.</p>"""
    target_table: NotRequired[
        "aws_sdk_glue.types.data_quality_target_table.DataQualityTargetTable"
    ]
    """<p>A target table associated with the data quality ruleset.</p>"""
    data_quality_security_configuration: NotRequired[
        "aws_sdk_glue.types.name_string.NameString"
    ]
    """<p>The name of the security configuration created with the data quality encryption option.</p>"""
    client_token: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataQualityRulesetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Ruleset"] = value["ruleset"]
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "target_table" in value:
        import aws_sdk_glue.types.data_quality_target_table

        out["TargetTable"] = (
            aws_sdk_glue.types.data_quality_target_table.serialize_aws_json_1_1(
                value["target_table"]
            )
        )
    if "data_quality_security_configuration" in value:
        out["DataQualitySecurityConfiguration"] = value[
            "data_quality_security_configuration"
        ]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataQualityRulesetRequest:
    out: CreateDataQualityRulesetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDataQualityRulesetRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Ruleset" in data:
        out["ruleset"] = data["Ruleset"]
    else:
        raise DeserializationError("CreateDataQualityRulesetRequest.ruleset required")
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if "TargetTable" in data:
        import aws_sdk_glue.types.data_quality_target_table

        out["target_table"] = (
            aws_sdk_glue.types.data_quality_target_table.deserialize_aws_json_1_1(
                data["TargetTable"]
            )
        )
    if "DataQualitySecurityConfiguration" in data:
        out["data_quality_security_configuration"] = data[
            "DataQualitySecurityConfiguration"
        ]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
