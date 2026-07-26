"""Generated from Smithy shape ``com.amazonaws.glue#SqlAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property_with_quote
    import capo_glue.types.node_id

SqlAlias = TypedDict(
    "SqlAlias",
    {
        "from": "capo_glue.types.node_id.NodeId",
        "alias": "capo_glue.types.enclosed_in_string_property_with_quote.EnclosedInStringPropertyWithQuote",
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlAlias) -> dict:
    out: dict = {}
    out["From"] = value["from"]
    out["Alias"] = value["alias"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlAlias:
    out: SqlAlias = {}  # type: ignore[typeddict-item]
    if "From" in data:
        out["from"] = data["From"]
    else:
        raise DeserializationError("SqlAlias.from required")
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("SqlAlias.alias required")
    return out
