"""Generated from Smithy shape ``com.amazonaws.glue#DeleteSecurityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.name_string


class DeleteSecurityConfigurationRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the security configuration to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSecurityConfigurationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSecurityConfigurationRequest:
    out: DeleteSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteSecurityConfigurationRequest.name required")
    return out
