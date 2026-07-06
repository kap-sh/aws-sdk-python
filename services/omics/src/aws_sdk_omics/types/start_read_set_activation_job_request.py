"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetActivationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.client_token
    import aws_sdk_omics.types.sequence_store_id
    import aws_sdk_omics.types.start_read_set_activation_job_source_list


class StartReadSetActivationJobRequest(TypedDict, closed=True):
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    client_token: NotRequired["aws_sdk_omics.types.client_token.ClientToken"]
    """<p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>"""
    sources: "aws_sdk_omics.types.start_read_set_activation_job_source_list.StartReadSetActivationJobSourceList"
    """<p>The job's source files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetActivationJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_omics.types.start_read_set_activation_job_source_list

    out["sources"] = (
        aws_sdk_omics.types.start_read_set_activation_job_source_list.serialize_json(
            value["sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartReadSetActivationJobRequest:
    out: StartReadSetActivationJobRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "sources" in data:
        import aws_sdk_omics.types.start_read_set_activation_job_source_list

        out["sources"] = (
            aws_sdk_omics.types.start_read_set_activation_job_source_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("StartReadSetActivationJobRequest.sources required")
    return out
