"""Generated from Smithy shape ``com.amazonaws.athena#ResultReuseInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boolean


class ResultReuseInformation(TypedDict, closed=True):
    reused_previous_result: "capo_athena.types.boolean.Boolean"
    """<p>True if a previous query result was reused; false if the result was generated from a new run of the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultReuseInformation) -> dict:
    out: dict = {}
    out["ReusedPreviousResult"] = value.get("reused_previous_result", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultReuseInformation:
    out: ResultReuseInformation = {}  # type: ignore[typeddict-item]
    if "ReusedPreviousResult" in data:
        out["reused_previous_result"] = data["ReusedPreviousResult"]
    else:
        out["reused_previous_result"] = False
    return out
