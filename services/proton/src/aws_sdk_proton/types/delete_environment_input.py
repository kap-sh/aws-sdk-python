"""Generated from Smithy shape ``com.amazonaws.proton#DeleteEnvironmentInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name


class DeleteEnvironmentInput(TypedDict):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the environment to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentInput:
    out: DeleteEnvironmentInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteEnvironmentInput.name required")
    return out
