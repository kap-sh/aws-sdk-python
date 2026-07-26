"""Generated from Smithy shape ``com.amazonaws.pipes#UpdatePipeSourceManagedStreamingKafkaParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.limit_max10000
    import capo_pipes.types.maximum_batching_window_in_seconds
    import capo_pipes.types.msk_access_credentials


class UpdatePipeSourceManagedStreamingKafkaParameters(TypedDict, closed=True):
    batch_size: NotRequired["capo_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    credentials: NotRequired[
        "capo_pipes.types.msk_access_credentials.MSKAccessCredentials"
    ]
    """<p>The credentials needed to access the resource.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "capo_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipeSourceManagedStreamingKafkaParameters) -> dict:
    out: dict = {}
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "credentials" in value:
        import capo_pipes.types.msk_access_credentials

        out["Credentials"] = capo_pipes.types.msk_access_credentials.serialize_json(
            value["credentials"]
        )
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    return out


def deserialize_json(data: dict) -> UpdatePipeSourceManagedStreamingKafkaParameters:
    out: UpdatePipeSourceManagedStreamingKafkaParameters = {}  # type: ignore[typeddict-item]
    if "BatchSize" in data:
        out["batch_size"] = data["BatchSize"]
    if "Credentials" in data:
        import capo_pipes.types.msk_access_credentials

        out["credentials"] = capo_pipes.types.msk_access_credentials.deserialize_json(
            data["Credentials"]
        )
    if "MaximumBatchingWindowInSeconds" in data:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    return out
