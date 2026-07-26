"""Generated from Smithy shape ``com.amazonaws.glue#DDBELTCatalogAdditionalOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boolean_value
    import capo_glue.types.enclosed_in_string_property


class DDBELTCatalogAdditionalOptions(TypedDict, closed=True):
    dynamodb_export: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies the DynamoDB export configuration for the ELT operation.</p>"""
    dynamodb_unnest_ddb_json: "capo_glue.types.boolean_value.BooleanValue"
    """<p>Specifies whether to unnest DynamoDB JSON format. When set to <code>true</code>, nested JSON structures in DynamoDB items are flattened.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DDBELTCatalogAdditionalOptions) -> dict:
    out: dict = {}
    if "dynamodb_export" in value:
        out["DynamodbExport"] = value["dynamodb_export"]
    out["DynamodbUnnestDDBJson"] = value.get("dynamodb_unnest_ddb_json", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DDBELTCatalogAdditionalOptions:
    out: DDBELTCatalogAdditionalOptions = {}  # type: ignore[typeddict-item]
    if "DynamodbExport" in data:
        out["dynamodb_export"] = data["DynamodbExport"]
    if "DynamodbUnnestDDBJson" in data:
        out["dynamodb_unnest_ddb_json"] = data["DynamodbUnnestDDBJson"]
    else:
        out["dynamodb_unnest_ddb_json"] = False
    return out
