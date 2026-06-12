"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.data_source


class CreateDataSourceResponse(TypedDict):
    data_source: "aws_sdk_bedrock_agent.types.data_source.DataSource"
    """<p>Contains details about the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.data_source

    out["dataSource"] = aws_sdk_bedrock_agent.types.data_source.serialize_json(
        value["data_source"]
    )
    return out


def deserialize_json(data: dict) -> CreateDataSourceResponse:
    out: CreateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "dataSource" in data:
        import aws_sdk_bedrock_agent.types.data_source

        out["data_source"] = aws_sdk_bedrock_agent.types.data_source.deserialize_json(
            data["dataSource"]
        )
    else:
        raise DeserializationError("CreateDataSourceResponse.data_source required")
    return out
