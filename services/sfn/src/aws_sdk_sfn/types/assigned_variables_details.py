"""Generated from Smithy shape ``com.amazonaws.sfn#AssignedVariablesDetails``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sfn.types.truncated


class AssignedVariablesDetails(TypedDict):
    truncated: "aws_sdk_sfn.types.truncated.truncated"
    """<p>Indicates whether assigned variables were truncated in the response. Always <code>false</code> for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssignedVariablesDetails) -> dict:
    out: dict = {}
    out["truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> AssignedVariablesDetails:
    out: AssignedVariablesDetails = {}  # type: ignore[typeddict-item]
    if "truncated" in data:
        out["truncated"] = data["truncated"]
    else:
        out["truncated"] = False
    return out
