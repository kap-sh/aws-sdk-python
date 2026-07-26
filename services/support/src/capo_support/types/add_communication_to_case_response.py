"""Generated from Smithy shape ``com.amazonaws.support#AddCommunicationToCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.result


class AddCommunicationToCaseResponse(TypedDict, closed=True):
    result: "capo_support.types.result.Result"
    """<p>True if <a>AddCommunicationToCase</a> succeeds. Otherwise, returns an error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddCommunicationToCaseResponse) -> dict:
    out: dict = {}
    out["result"] = value.get("result", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> AddCommunicationToCaseResponse:
    out: AddCommunicationToCaseResponse = {}  # type: ignore[typeddict-item]
    if "result" in data:
        out["result"] = data["result"]
    else:
        out["result"] = False
    return out
