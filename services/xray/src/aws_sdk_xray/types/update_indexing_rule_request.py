"""Generated from Smithy shape ``com.amazonaws.xray#UpdateIndexingRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.indexing_rule_value_update
    import aws_sdk_xray.types.string


class UpdateIndexingRuleRequest(TypedDict):
    name: "aws_sdk_xray.types.string.String"
    """<p> Name of the indexing rule to be updated. </p>"""
    rule: "aws_sdk_xray.types.indexing_rule_value_update.IndexingRuleValueUpdate"
    """<p> Rule configuration to be updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexingRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_xray.types.indexing_rule_value_update

    out["Rule"] = aws_sdk_xray.types.indexing_rule_value_update.serialize_json(
        value["rule"]
    )
    return out


def deserialize_json(data: dict) -> UpdateIndexingRuleRequest:
    out: UpdateIndexingRuleRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateIndexingRuleRequest.name required")
    if "Rule" in data:
        import aws_sdk_xray.types.indexing_rule_value_update

        out["rule"] = aws_sdk_xray.types.indexing_rule_value_update.deserialize_json(
            data["Rule"]
        )
    else:
        raise DeserializationError("UpdateIndexingRuleRequest.rule required")
    return out
