"""Generated from Smithy shape ``com.amazonaws.cleanrooms#WorkerComputeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.worker_compute_configuration_properties
    import aws_sdk_cleanrooms.types.worker_compute_type


class WorkerComputeConfiguration(TypedDict):
    type: NotRequired["aws_sdk_cleanrooms.types.worker_compute_type.WorkerComputeType"]
    """<p> The worker compute configuration type.</p>"""
    number: NotRequired["int"]
    """<p> The number of workers.</p> <p>SQL queries support a minimum value of 2 and a maximum value of 400. </p> <p>PySpark jobs support a minimum value of 4 and a maximum value of 128.</p>"""
    properties: NotRequired[
        "aws_sdk_cleanrooms.types.worker_compute_configuration_properties.WorkerComputeConfigurationProperties"
    ]
    """<p>The configuration properties for the worker compute environment. These properties allow you to customize the compute settings for your Clean Rooms workloads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerComputeConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.worker_compute_type

    out["type"] = aws_sdk_cleanrooms.types.worker_compute_type.serialize_json(
        value.get("type", "CR.1X")
    )
    out["number"] = value.get("number", 16)
    if "properties" in value:
        import aws_sdk_cleanrooms.types.worker_compute_configuration_properties

        out["properties"] = (
            aws_sdk_cleanrooms.types.worker_compute_configuration_properties.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkerComputeConfiguration:
    out: WorkerComputeConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_cleanrooms.types.worker_compute_type

        out["type"] = aws_sdk_cleanrooms.types.worker_compute_type.deserialize_json(
            data["type"]
        )
    else:
        out["type"] = "CR.1X"
    if "number" in data:
        out["number"] = data["number"]
    else:
        out["number"] = 16
    if "properties" in data:
        import aws_sdk_cleanrooms.types.worker_compute_configuration_properties

        out["properties"] = (
            aws_sdk_cleanrooms.types.worker_compute_configuration_properties.deserialize_json(
                data["properties"]
            )
        )
    return out
