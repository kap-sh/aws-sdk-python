"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#SchemaElementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.schema_element

SchemaElementList: TypeAlias = list[
    "aws_sdk_cost_and_usage_report_service.types.schema_element.SchemaElement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaElementList) -> list:
    import aws_sdk_cost_and_usage_report_service.types.schema_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_and_usage_report_service.types.schema_element.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SchemaElementList:
    import aws_sdk_cost_and_usage_report_service.types.schema_element

    out: SchemaElementList = []
    for item in data:
        out.append(
            aws_sdk_cost_and_usage_report_service.types.schema_element.deserialize_aws_json_1_1(
                item
            )
        )
    return out
