"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateRuleMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.rule


class UpdateRuleMetadataRequest(TypedDict, closed=True):
    rule: "aws_sdk_frauddetector.types.rule.Rule"
    """<p>The rule to update.</p>"""
    description: "aws_sdk_frauddetector.types.description.description"
    """<p>The rule description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuleMetadataRequest) -> dict:
    out: dict = {}
    import aws_sdk_frauddetector.types.rule

    out["rule"] = aws_sdk_frauddetector.types.rule.serialize_aws_json_1_1(value["rule"])
    out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuleMetadataRequest:
    out: UpdateRuleMetadataRequest = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import aws_sdk_frauddetector.types.rule

        out["rule"] = aws_sdk_frauddetector.types.rule.deserialize_aws_json_1_1(
            data["rule"]
        )
    else:
        raise DeserializationError("UpdateRuleMetadataRequest.rule required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("UpdateRuleMetadataRequest.description required")
    return out
