"""Generated from Smithy shape ``com.amazonaws.datazone#StartNotebookRunInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.compute_config
    import capo_datazone.types.domain_id
    import capo_datazone.types.metadata
    import capo_datazone.types.network_config
    import capo_datazone.types.notebook_id
    import capo_datazone.types.parameters
    import capo_datazone.types.project_id
    import capo_datazone.types.schedule_id
    import capo_datazone.types.timeout_config
    import capo_datazone.types.trigger_source


class StartNotebookRunInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is started.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook run.</p>"""
    notebook_identifier: "capo_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook to run.</p>"""
    schedule_identifier: NotRequired["capo_datazone.types.schedule_id.ScheduleId"]
    """<p>The identifier of the schedule associated with the notebook run.</p>"""
    compute_configuration: NotRequired[
        "capo_datazone.types.compute_config.ComputeConfig"
    ]
    """<p>The compute configuration for the notebook run, including instance type and environment version.</p>"""
    network_configuration: NotRequired[
        "capo_datazone.types.network_config.NetworkConfig"
    ]
    """<p>The network configuration for the notebook run, including network access type and optional VPC settings.</p>"""
    timeout_configuration: NotRequired[
        "capo_datazone.types.timeout_config.TimeoutConfig"
    ]
    """<p>The timeout configuration for the notebook run. The default timeout is 720 minutes (12 hours) and the maximum is 1440 minutes (24 hours).</p>"""
    trigger_source: NotRequired["capo_datazone.types.trigger_source.TriggerSource"]
    """<p>The source that triggered the notebook run.</p>"""
    metadata: NotRequired["capo_datazone.types.metadata.Metadata"]
    """<p>The metadata for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>"""
    parameters: NotRequired["capo_datazone.types.parameters.Parameters"]
    """<p>The sensitive parameters for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNotebookRunInput) -> dict:
    out: dict = {}
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    out["notebookIdentifier"] = value["notebook_identifier"]
    if "schedule_identifier" in value:
        out["scheduleIdentifier"] = value["schedule_identifier"]
    if "compute_configuration" in value:
        import capo_datazone.types.compute_config

        out["computeConfiguration"] = capo_datazone.types.compute_config.serialize_json(
            value["compute_configuration"]
        )
    if "network_configuration" in value:
        import capo_datazone.types.network_config

        out["networkConfiguration"] = capo_datazone.types.network_config.serialize_json(
            value["network_configuration"]
        )
    if "timeout_configuration" in value:
        import capo_datazone.types.timeout_config

        out["timeoutConfiguration"] = capo_datazone.types.timeout_config.serialize_json(
            value["timeout_configuration"]
        )
    if "trigger_source" in value:
        import capo_datazone.types.trigger_source

        out["triggerSource"] = capo_datazone.types.trigger_source.serialize_json(
            value["trigger_source"]
        )
    if "metadata" in value:
        import capo_datazone.types.metadata

        out["metadata"] = capo_datazone.types.metadata.serialize_json(value["metadata"])
    if "parameters" in value:
        import capo_datazone.types.parameters

        out["parameters"] = capo_datazone.types.parameters.serialize_json(
            value["parameters"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartNotebookRunInput:
    out: StartNotebookRunInput = {}  # type: ignore[typeddict-item]
    if "owningProjectIdentifier" in data:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartNotebookRunInput.owning_project_identifier required"
        )
    if "notebookIdentifier" in data:
        out["notebook_identifier"] = data["notebookIdentifier"]
    else:
        raise DeserializationError("StartNotebookRunInput.notebook_identifier required")
    if "scheduleIdentifier" in data:
        out["schedule_identifier"] = data["scheduleIdentifier"]
    if "computeConfiguration" in data:
        import capo_datazone.types.compute_config

        out["compute_configuration"] = (
            capo_datazone.types.compute_config.deserialize_json(
                data["computeConfiguration"]
            )
        )
    if "networkConfiguration" in data:
        import capo_datazone.types.network_config

        out["network_configuration"] = (
            capo_datazone.types.network_config.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if "timeoutConfiguration" in data:
        import capo_datazone.types.timeout_config

        out["timeout_configuration"] = (
            capo_datazone.types.timeout_config.deserialize_json(
                data["timeoutConfiguration"]
            )
        )
    if "triggerSource" in data:
        import capo_datazone.types.trigger_source

        out["trigger_source"] = capo_datazone.types.trigger_source.deserialize_json(
            data["triggerSource"]
        )
    if "metadata" in data:
        import capo_datazone.types.metadata

        out["metadata"] = capo_datazone.types.metadata.deserialize_json(
            data["metadata"]
        )
    if "parameters" in data:
        import capo_datazone.types.parameters

        out["parameters"] = capo_datazone.types.parameters.deserialize_json(
            data["parameters"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
