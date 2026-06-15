"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingsStatisticsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_arn


class GetFindingsStatisticsRequest(TypedDict):
    analyzer_arn: "aws_sdk_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources\">ARN of the analyzer</a> used to generate the statistics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsStatisticsRequest) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    return out


def deserialize_json(data: dict) -> GetFindingsStatisticsRequest:
    out: GetFindingsStatisticsRequest = {}  # type: ignore[typeddict-item]
    if "analyzerArn" in data:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        raise DeserializationError("GetFindingsStatisticsRequest.analyzer_arn required")
    return out
