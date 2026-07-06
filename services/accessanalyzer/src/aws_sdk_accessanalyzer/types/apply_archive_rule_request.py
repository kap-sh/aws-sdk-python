"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ApplyArchiveRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_arn
    import aws_sdk_accessanalyzer.types.name


class ApplyArchiveRuleRequest(TypedDict, closed=True):
    analyzer_arn: "aws_sdk_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The Amazon resource name (ARN) of the analyzer.</p>"""
    rule_name: "aws_sdk_accessanalyzer.types.name.Name"
    """<p>The name of the rule to apply.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplyArchiveRuleRequest) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    out["ruleName"] = value["rule_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ApplyArchiveRuleRequest:
    out: ApplyArchiveRuleRequest = {}  # type: ignore[typeddict-item]
    if "analyzerArn" in data:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        raise DeserializationError("ApplyArchiveRuleRequest.analyzer_arn required")
    if "ruleName" in data:
        out["rule_name"] = data["ruleName"]
    else:
        raise DeserializationError("ApplyArchiveRuleRequest.rule_name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
