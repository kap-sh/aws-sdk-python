"""Generated from Smithy shape ``com.amazonaws.emr#DeleteSecurityConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string


class DeleteSecurityConfigurationInput(TypedDict):
    name: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The name of the security configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSecurityConfigurationInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSecurityConfigurationInput:
    out: DeleteSecurityConfigurationInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
