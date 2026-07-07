"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name


class DeleteServiceTemplateInput(TypedDict, closed=True):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service template to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceTemplateInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceTemplateInput:
    out: DeleteServiceTemplateInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteServiceTemplateInput.name required")
    return out
