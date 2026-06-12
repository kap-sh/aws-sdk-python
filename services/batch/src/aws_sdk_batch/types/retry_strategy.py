"""Generated from Smithy shape ``com.amazonaws.batch#RetryStrategy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.evaluate_on_exit_list
    import aws_sdk_batch.types.integer


class RetryStrategy(TypedDict):
    attempts: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The number of times to move a job to the <code>RUNNABLE</code> status. You can specify between 1 and 10 attempts. If the value of <code>attempts</code> is greater than one, the job is retried on failure the same number of attempts as the value.</p>"""
    evaluate_on_exit: NotRequired[
        "aws_sdk_batch.types.evaluate_on_exit_list.EvaluateOnExitList"
    ]
    """<p>Array of up to 5 objects that specify the conditions where jobs are retried or failed. If this parameter is specified, then the <code>attempts</code> parameter must also be specified. If none of the listed conditions match, then the job is retried.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryStrategy) -> dict:
    out: dict = {}
    if "attempts" in value:
        out["attempts"] = value["attempts"]
    if "evaluate_on_exit" in value:
        import aws_sdk_batch.types.evaluate_on_exit_list

        out["evaluateOnExit"] = (
            aws_sdk_batch.types.evaluate_on_exit_list.serialize_json(
                value["evaluate_on_exit"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetryStrategy:
    out: RetryStrategy = {}  # type: ignore[typeddict-item]
    if "attempts" in data:
        out["attempts"] = data["attempts"]
    if "evaluateOnExit" in data:
        import aws_sdk_batch.types.evaluate_on_exit_list

        out["evaluate_on_exit"] = (
            aws_sdk_batch.types.evaluate_on_exit_list.deserialize_json(
                data["evaluateOnExit"]
            )
        )
    return out
