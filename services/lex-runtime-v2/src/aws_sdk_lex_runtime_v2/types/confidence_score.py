"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ConfidenceScore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.double


class ConfidenceScore(TypedDict, closed=True):
    score: "aws_sdk_lex_runtime_v2.types.double.Double"
    """<p>A score that indicates how confident Amazon Lex V2 is that an intent satisfies the user's intent. Ranges between 0.00 and 1.00. Higher scores indicate higher confidence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfidenceScore) -> dict:
    out: dict = {}
    out["score"] = value.get("score", 0)
    return out


def deserialize_json(data: dict) -> ConfidenceScore:
    out: ConfidenceScore = {}  # type: ignore[typeddict-item]
    if "score" in data:
        out["score"] = data["score"]
    else:
        out["score"] = 0
    return out
