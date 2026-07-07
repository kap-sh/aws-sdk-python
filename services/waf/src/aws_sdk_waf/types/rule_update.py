"""Generated from Smithy shape ``com.amazonaws.waf#RuleUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_action
    import aws_sdk_waf.types.predicate


class RuleUpdate(TypedDict, closed=True):
    action: "aws_sdk_waf.types.change_action.ChangeAction"
    """<p>Specify <code>INSERT</code> to add a <code>Predicate</code> to a <code>Rule</code>. Use <code>DELETE</code> to remove a <code>Predicate</code> from a <code>Rule</code>.</p>"""
    predicate: "aws_sdk_waf.types.predicate.Predicate"
    """<p>The ID of the <code>Predicate</code> (such as an <code>IPSet</code>) that you want to add to a <code>Rule</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleUpdate) -> dict:
    out: dict = {}
    import aws_sdk_waf.types.change_action

    out["Action"] = aws_sdk_waf.types.change_action.serialize_aws_json_1_1(
        value["action"]
    )
    import aws_sdk_waf.types.predicate

    out["Predicate"] = aws_sdk_waf.types.predicate.serialize_aws_json_1_1(
        value["predicate"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleUpdate:
    out: RuleUpdate = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_waf.types.change_action

        out["action"] = aws_sdk_waf.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("RuleUpdate.action required")
    if "Predicate" in data:
        import aws_sdk_waf.types.predicate

        out["predicate"] = aws_sdk_waf.types.predicate.deserialize_aws_json_1_1(
            data["Predicate"]
        )
    else:
        raise DeserializationError("RuleUpdate.predicate required")
    return out
