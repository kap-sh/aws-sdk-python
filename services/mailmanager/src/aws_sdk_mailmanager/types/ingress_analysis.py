"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.analyzer_arn
    import aws_sdk_mailmanager.types.result_field


class IngressAnalysis(TypedDict, closed=True):
    analyzer: "aws_sdk_mailmanager.types.analyzer_arn.AnalyzerArn"
    """<p>The Amazon Resource Name (ARN) of an Add On.</p>"""
    result_field: "aws_sdk_mailmanager.types.result_field.ResultField"
    """<p>The returned value from an Add On.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressAnalysis) -> dict:
    out: dict = {}
    out["Analyzer"] = value["analyzer"]
    out["ResultField"] = value["result_field"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressAnalysis:
    out: IngressAnalysis = {}  # type: ignore[typeddict-item]
    if "Analyzer" in data:
        out["analyzer"] = data["Analyzer"]
    else:
        raise DeserializationError("IngressAnalysis.analyzer required")
    if "ResultField" in data:
        out["result_field"] = data["ResultField"]
    else:
        raise DeserializationError("IngressAnalysis.result_field required")
    return out
