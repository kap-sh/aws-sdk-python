"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.data_source


class UpdateDataSourceResponse(TypedDict, closed=True):
    data_source: "capo_bedrock_agent.types.data_source.DataSource"
    """<p>Contains details about the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.data_source

    out["dataSource"] = capo_bedrock_agent.types.data_source.serialize_json(
        value["data_source"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataSourceResponse:
    out: UpdateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "dataSource" in data:
        import capo_bedrock_agent.types.data_source

        out["data_source"] = capo_bedrock_agent.types.data_source.deserialize_json(
            data["dataSource"]
        )
    else:
        raise DeserializationError("UpdateDataSourceResponse.data_source required")
    return out
