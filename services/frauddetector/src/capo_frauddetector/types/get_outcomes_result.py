"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetOutcomesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.outcome_list
    import capo_frauddetector.types.string


class GetOutcomesResult(TypedDict, closed=True):
    outcomes: NotRequired["capo_frauddetector.types.outcome_list.OutcomeList"]
    """<p>The outcomes. </p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next page token for subsequent requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOutcomesResult) -> dict:
    out: dict = {}
    if "outcomes" in value:
        import capo_frauddetector.types.outcome_list

        out["outcomes"] = capo_frauddetector.types.outcome_list.serialize_aws_json_1_1(
            value["outcomes"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOutcomesResult:
    out: GetOutcomesResult = {}  # type: ignore[typeddict-item]
    if "outcomes" in data:
        import capo_frauddetector.types.outcome_list

        out["outcomes"] = (
            capo_frauddetector.types.outcome_list.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
