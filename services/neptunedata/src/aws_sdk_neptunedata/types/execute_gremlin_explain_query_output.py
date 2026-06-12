"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteGremlinExplainQueryOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.report_as_text

class ExecuteGremlinExplainQueryOutput(TypedDict):
    output: NotRequired["aws_sdk_neptunedata.types.report_as_text.ReportAsText"]
    """<p>A text blob containing the Gremlin explain result, as described in <a href=\"https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-traversal-tuning.html\">Tuning Gremlin queries</a>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ExecuteGremlinExplainQueryOutput) -> dict:
    out: dict = {}
    if "output" in value:
        import aws_sdk_neptunedata.types.report_as_text
        out["output"] = aws_sdk_neptunedata.types.report_as_text.serialize_json(value["output"])
    return out


def deserialize_json(data: dict) -> ExecuteGremlinExplainQueryOutput:
    out: ExecuteGremlinExplainQueryOutput = {}  # type: ignore[typeddict-item]
    if "output" in data:
        import aws_sdk_neptunedata.types.report_as_text
        out["output"] = aws_sdk_neptunedata.types.report_as_text.deserialize_json(data["output"])
    return out