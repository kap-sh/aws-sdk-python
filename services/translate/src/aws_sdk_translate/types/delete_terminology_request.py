"""Generated from Smithy shape ``com.amazonaws.translate#DeleteTerminologyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.resource_name


class DeleteTerminologyRequest(TypedDict):
    name: "aws_sdk_translate.types.resource_name.ResourceName"
    """<p>The name of the custom terminology being deleted. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTerminologyRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTerminologyRequest:
    out: DeleteTerminologyRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteTerminologyRequest.name required")
    return out
