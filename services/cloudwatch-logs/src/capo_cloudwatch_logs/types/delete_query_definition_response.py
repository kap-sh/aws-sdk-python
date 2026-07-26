"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteQueryDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.success


class DeleteQueryDefinitionResponse(TypedDict, closed=True):
    success: "capo_cloudwatch_logs.types.success.Success"
    """<p>A value of TRUE indicates that the operation succeeded. FALSE indicates that the operation failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteQueryDefinitionResponse) -> dict:
    out: dict = {}
    out["success"] = value.get("success", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteQueryDefinitionResponse:
    out: DeleteQueryDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "success" in data:
        out["success"] = data["success"]
    else:
        out["success"] = False
    return out
