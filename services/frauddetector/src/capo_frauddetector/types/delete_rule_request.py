"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.rule


class DeleteRuleRequest(TypedDict, closed=True):
    rule: "capo_frauddetector.types.rule.Rule"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRuleRequest) -> dict:
    out: dict = {}
    import capo_frauddetector.types.rule

    out["rule"] = capo_frauddetector.types.rule.serialize_aws_json_1_1(value["rule"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRuleRequest:
    out: DeleteRuleRequest = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import capo_frauddetector.types.rule

        out["rule"] = capo_frauddetector.types.rule.deserialize_aws_json_1_1(
            data["rule"]
        )
    else:
        raise DeserializationError("DeleteRuleRequest.rule required")
    return out
