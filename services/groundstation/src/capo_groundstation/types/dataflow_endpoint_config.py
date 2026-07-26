"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowEndpointConfig``."""

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError


class DataflowEndpointConfig(TypedDict, closed=True):
    dataflow_endpoint_name: "str"
    """<p>Name of a dataflow endpoint.</p>"""
    dataflow_endpoint_region: NotRequired["str"]
    """<p>Region of a dataflow endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataflowEndpointConfig) -> dict:
    out: dict = {}
    out["dataflowEndpointName"] = value["dataflow_endpoint_name"]
    if "dataflow_endpoint_region" in value:
        out["dataflowEndpointRegion"] = value["dataflow_endpoint_region"]
    return out


def deserialize_json(data: dict) -> DataflowEndpointConfig:
    out: DataflowEndpointConfig = {}  # type: ignore[typeddict-item]
    if "dataflowEndpointName" in data:
        out["dataflow_endpoint_name"] = data["dataflowEndpointName"]
    else:
        raise DeserializationError(
            "DataflowEndpointConfig.dataflow_endpoint_name required"
        )
    if "dataflowEndpointRegion" in data:
        out["dataflow_endpoint_region"] = data["dataflowEndpointRegion"]
    return out
