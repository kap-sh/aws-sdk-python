"""Generated from Smithy shape ``com.amazonaws.datazone#CloudFormationProperties``."""

from typing import TypedDict

from aws_sdk_datazone.errors import DeserializationError


class CloudFormationProperties(TypedDict):
    template_url: "str"
    """<p>The template URL of the cloud formation provisioning properties of the environment blueprint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudFormationProperties) -> dict:
    out: dict = {}
    out["templateUrl"] = value["template_url"]
    return out


def deserialize_json(data: dict) -> CloudFormationProperties:
    out: CloudFormationProperties = {}  # type: ignore[typeddict-item]
    if "templateUrl" in data:
        out["template_url"] = data["templateUrl"]
    else:
        raise DeserializationError("CloudFormationProperties.template_url required")
    return out
