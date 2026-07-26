"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#WorkerComputeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.worker_compute_configuration_properties
    import capo_cleanroomsml.types.worker_compute_type


class WorkerComputeConfiguration(TypedDict, closed=True):
    type: "capo_cleanroomsml.types.worker_compute_type.WorkerComputeType"
    """<p>The instance type of the compute workers that are used.</p>"""
    number: "int"
    """<p>The number of compute workers that are used.</p>"""
    properties: NotRequired[
        "capo_cleanroomsml.types.worker_compute_configuration_properties.WorkerComputeConfigurationProperties"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: WorkerComputeConfiguration) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.worker_compute_type

    out["type"] = capo_cleanroomsml.types.worker_compute_type.serialize_json(
        value.get("type", "CR.1X")
    )
    out["number"] = value.get("number", 16)
    if "properties" in value:
        import capo_cleanroomsml.types.worker_compute_configuration_properties

        out["properties"] = (
            capo_cleanroomsml.types.worker_compute_configuration_properties.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkerComputeConfiguration:
    out: WorkerComputeConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_cleanroomsml.types.worker_compute_type

        out["type"] = capo_cleanroomsml.types.worker_compute_type.deserialize_json(
            data["type"]
        )
    else:
        out["type"] = "CR.1X"
    if "number" in data:
        out["number"] = data["number"]
    else:
        out["number"] = 16
    if "properties" in data:
        import capo_cleanroomsml.types.worker_compute_configuration_properties

        out["properties"] = (
            capo_cleanroomsml.types.worker_compute_configuration_properties.deserialize_json(
                data["properties"]
            )
        )
    return out
