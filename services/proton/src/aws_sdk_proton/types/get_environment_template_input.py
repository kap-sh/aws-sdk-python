"""Generated from Smithy shape ``com.amazonaws.proton#GetEnvironmentTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name


class GetEnvironmentTemplateInput(TypedDict):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template that you want to get the detailed data for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentTemplateInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentTemplateInput:
    out: GetEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetEnvironmentTemplateInput.name required")
    return out
