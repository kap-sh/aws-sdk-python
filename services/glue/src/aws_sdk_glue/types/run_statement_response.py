"""Generated from Smithy shape ``com.amazonaws.glue#RunStatementResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.integer_value


class RunStatementResponse(TypedDict):
    id: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>Returns the Id of the statement that was run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunStatementResponse) -> dict:
    out: dict = {}
    out["Id"] = value.get("id", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> RunStatementResponse:
    out: RunStatementResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        out["id"] = 0
    return out
