"""Generated from Smithy shape ``com.amazonaws.budgets#TimePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_budgets.types.generic_timestamp


class TimePeriod(TypedDict, closed=True):
    start: NotRequired["aws_sdk_budgets.types.generic_timestamp.GenericTimestamp"]
    """<p>The start date for a budget. If you created your budget and didn't specify a start date, Amazon Web Services defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, ANNUALLY, or CUSTOM). For example, if you created your budget on January 24, 2018, chose <code>DAILY</code>, and didn't set a start date, Amazon Web Services set your start date to <code>01/24/18 00:00 UTC</code>. If you chose <code>MONTHLY</code>, Amazon Web Services set your start date to <code>01/01/18 00:00 UTC</code>. The defaults are the same for the Billing and Cost Management console and the API.</p> <p>You can change your start date with the <code>UpdateBudget</code> operation.</p>"""
    end: NotRequired["aws_sdk_budgets.types.generic_timestamp.GenericTimestamp"]
    """<p>The end date for a budget. If you didn't specify an end date, Amazon Web Services set your end date to <code>06/15/87 00:00 UTC</code>. The defaults are the same for the Billing and Cost Management console and the API.</p> <p>After the end date, Amazon Web Services deletes the budget and all the associated notifications and subscribers. You can change your end date with the <code>UpdateBudget</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimePeriod) -> dict:
    out: dict = {}
    if "start" in value:
        import aws_sdk_budgets.types.generic_timestamp

        out["Start"] = aws_sdk_budgets.types.generic_timestamp.serialize_aws_json_1_1(
            value["start"]
        )
    if "end" in value:
        import aws_sdk_budgets.types.generic_timestamp

        out["End"] = aws_sdk_budgets.types.generic_timestamp.serialize_aws_json_1_1(
            value["end"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if "Start" in data:
        import aws_sdk_budgets.types.generic_timestamp

        out["start"] = aws_sdk_budgets.types.generic_timestamp.deserialize_aws_json_1_1(
            data["Start"]
        )
    if "End" in data:
        import aws_sdk_budgets.types.generic_timestamp

        out["end"] = aws_sdk_budgets.types.generic_timestamp.deserialize_aws_json_1_1(
            data["End"]
        )
    return out
