"""Generated from Smithy shape ``com.amazonaws.datazone#HyperPodPropertiesInput``."""

from typing import TypedDict
from aws_sdk_datazone.errors import DeserializationError


class HyperPodPropertiesInput(TypedDict):
    cluster_name: "str"
    """<p>The cluster name the hyper pod properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HyperPodPropertiesInput) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    return out


def deserialize_json(data: dict) -> HyperPodPropertiesInput:
    out: HyperPodPropertiesInput = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    else:
        raise DeserializationError("HyperPodPropertiesInput.cluster_name required")
    return out
