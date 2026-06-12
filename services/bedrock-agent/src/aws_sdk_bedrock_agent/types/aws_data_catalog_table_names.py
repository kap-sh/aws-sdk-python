"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AwsDataCatalogTableNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.aws_data_catalog_table_name

AwsDataCatalogTableNames: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.aws_data_catalog_table_name.AwsDataCatalogTableName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDataCatalogTableNames) -> list:
    return list(value)


def deserialize_json(data: list) -> AwsDataCatalogTableNames:
    return list(data)
