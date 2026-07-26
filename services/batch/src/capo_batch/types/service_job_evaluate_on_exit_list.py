"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobEvaluateOnExitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.service_job_evaluate_on_exit

ServiceJobEvaluateOnExitList: TypeAlias = list[
    "capo_batch.types.service_job_evaluate_on_exit.ServiceJobEvaluateOnExit"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobEvaluateOnExitList) -> list:
    import capo_batch.types.service_job_evaluate_on_exit

    out: list = []
    for item in value:
        out.append(capo_batch.types.service_job_evaluate_on_exit.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceJobEvaluateOnExitList:
    import capo_batch.types.service_job_evaluate_on_exit

    out: ServiceJobEvaluateOnExitList = []
    for item in data:
        out.append(capo_batch.types.service_job_evaluate_on_exit.deserialize_json(item))
    return out
