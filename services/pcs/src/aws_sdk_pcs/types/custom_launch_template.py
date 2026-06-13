"""Generated from Smithy shape ``com.amazonaws.pcs#CustomLaunchTemplate``."""

from typing import TypedDict

from aws_sdk_pcs.errors import DeserializationError


class CustomLaunchTemplate(TypedDict):
    id: "str"
    """<p>The ID of the EC2 launch template to use to provision instances.</p> <p> Example: <code>lt-xxxx</code> </p>"""
    version: "str"
    """<p>The version of the EC2 launch template to use to provision instances.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomLaunchTemplate) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomLaunchTemplate:
    out: CustomLaunchTemplate = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CustomLaunchTemplate.id required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CustomLaunchTemplate.version required")
    return out
