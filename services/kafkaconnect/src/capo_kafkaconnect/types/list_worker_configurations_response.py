"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ListWorkerConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__list_of_worker_configuration_summary
    import capo_kafkaconnect.types.__string


class ListWorkerConfigurationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>If the response of a ListWorkerConfigurations operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.</p>"""
    worker_configurations: NotRequired[
        "capo_kafkaconnect.types.__list_of_worker_configuration_summary.__listOfWorkerConfigurationSummary"
    ]
    """<p>An array of worker configuration descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkerConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "worker_configurations" in value:
        import capo_kafkaconnect.types.__list_of_worker_configuration_summary

        out["workerConfigurations"] = (
            capo_kafkaconnect.types.__list_of_worker_configuration_summary.serialize_json(
                value["worker_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListWorkerConfigurationsResponse:
    out: ListWorkerConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "workerConfigurations" in data:
        import capo_kafkaconnect.types.__list_of_worker_configuration_summary

        out["worker_configurations"] = (
            capo_kafkaconnect.types.__list_of_worker_configuration_summary.deserialize_json(
                data["workerConfigurations"]
            )
        )
    return out
