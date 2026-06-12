"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetOutcomesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.outcome_list
    import aws_sdk_frauddetector.types.string


class GetOutcomesResult(TypedDict):
    outcomes: NotRequired["aws_sdk_frauddetector.types.outcome_list.OutcomeList"]
    """<p>The outcomes. </p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next page token for subsequent requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOutcomesResult) -> dict:
    out: dict = {}
    if "outcomes" in value:
        import aws_sdk_frauddetector.types.outcome_list

        out["outcomes"] = (
            aws_sdk_frauddetector.types.outcome_list.serialize_aws_json_1_1(
                value["outcomes"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOutcomesResult:
    out: GetOutcomesResult = {}  # type: ignore[typeddict-item]
    if "outcomes" in data:
        import aws_sdk_frauddetector.types.outcome_list

        out["outcomes"] = (
            aws_sdk_frauddetector.types.outcome_list.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
