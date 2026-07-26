"""Generated from Smithy shape ``com.amazonaws.redshiftdata#CancelStatementResponse``."""

from typing_extensions import NotRequired, TypedDict


class CancelStatementResponse(TypedDict, closed=True):
    status: NotRequired["bool"]
    """<p>A value that indicates whether the cancel statement succeeded (true). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelStatementResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelStatementResponse:
    out: CancelStatementResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
