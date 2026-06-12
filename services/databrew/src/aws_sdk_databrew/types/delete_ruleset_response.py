"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteRulesetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.ruleset_name


class DeleteRulesetResponse(TypedDict):
    name: "aws_sdk_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the deleted ruleset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRulesetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteRulesetResponse:
    out: DeleteRulesetResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteRulesetResponse.name required")
    return out
