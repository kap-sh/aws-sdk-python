"""Generated from Smithy shape ``com.amazonaws.databrew#CreateRulesetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.ruleset_name


class CreateRulesetResponse(TypedDict):
    name: "aws_sdk_databrew.types.ruleset_name.RulesetName"
    """<p>The unique name of the created ruleset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRulesetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateRulesetResponse:
    out: CreateRulesetResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRulesetResponse.name required")
    return out
