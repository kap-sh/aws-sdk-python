"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateRulesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.ruleset_name


class UpdateRulesetResponse(TypedDict, closed=True):
    name: "capo_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the updated ruleset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRulesetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateRulesetResponse:
    out: UpdateRulesetResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateRulesetResponse.name required")
    return out
