"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobRetryStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.service_job_evaluate_on_exit_list


class ServiceJobRetryStrategy(TypedDict, closed=True):
    attempts: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The number of times to move a service job to <code>RUNNABLE</code> status. You can specify between 1 and 10 attempts.</p>"""
    evaluate_on_exit: NotRequired[
        "capo_batch.types.service_job_evaluate_on_exit_list.ServiceJobEvaluateOnExitList"
    ]
    """<p>Array of <code>ServiceJobEvaluateOnExit</code> objects that specify conditions under which the service job should be retried or failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobRetryStrategy) -> dict:
    out: dict = {}
    if "attempts" in value:
        out["attempts"] = value["attempts"]
    if "evaluate_on_exit" in value:
        import capo_batch.types.service_job_evaluate_on_exit_list

        out["evaluateOnExit"] = (
            capo_batch.types.service_job_evaluate_on_exit_list.serialize_json(
                value["evaluate_on_exit"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceJobRetryStrategy:
    out: ServiceJobRetryStrategy = {}  # type: ignore[typeddict-item]
    if "attempts" in data:
        out["attempts"] = data["attempts"]
    if "evaluateOnExit" in data:
        import capo_batch.types.service_job_evaluate_on_exit_list

        out["evaluate_on_exit"] = (
            capo_batch.types.service_job_evaluate_on_exit_list.deserialize_json(
                data["evaluateOnExit"]
            )
        )
    return out
