"""Generated from Smithy shape ``com.amazonaws.devopsagent#ReferenceOutput``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError


class ReferenceOutput(TypedDict, closed=True):
    system: "str"
    """<p>The name of the external system</p>"""
    title: NotRequired["str"]
    """<p>Optional title for the reference</p>"""
    reference_id: "str"
    """<p>The unique identifier in the external system</p>"""
    reference_url: "str"
    """<p>URL to access the reference in the external system</p>"""
    association_id: "str"
    """<p>Association identifier of the external system</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceOutput) -> dict:
    out: dict = {}
    out["system"] = value["system"]
    if "title" in value:
        out["title"] = value["title"]
    out["referenceId"] = value["reference_id"]
    out["referenceUrl"] = value["reference_url"]
    out["associationId"] = value["association_id"]
    return out


def deserialize_json(data: dict) -> ReferenceOutput:
    out: ReferenceOutput = {}  # type: ignore[typeddict-item]
    if "system" in data:
        out["system"] = data["system"]
    else:
        raise DeserializationError("ReferenceOutput.system required")
    if "title" in data:
        out["title"] = data["title"]
    if "referenceId" in data:
        out["reference_id"] = data["referenceId"]
    else:
        raise DeserializationError("ReferenceOutput.reference_id required")
    if "referenceUrl" in data:
        out["reference_url"] = data["referenceUrl"]
    else:
        raise DeserializationError("ReferenceOutput.reference_url required")
    if "associationId" in data:
        out["association_id"] = data["associationId"]
    else:
        raise DeserializationError("ReferenceOutput.association_id required")
    return out
