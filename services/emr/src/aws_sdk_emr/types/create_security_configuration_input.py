"""Generated from Smithy shape ``com.amazonaws.emr#CreateSecurityConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.xml_string


class CreateSecurityConfigurationInput(TypedDict):
    name: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The name of the security configuration.</p>"""
    security_configuration: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The security configuration details in JSON format. For JSON parameters and examples, see <a href=\"https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-security-configurations.html\">Use Security Configurations to Set Up Cluster Security</a> in the <i>Amazon EMR Management Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSecurityConfigurationInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSecurityConfigurationInput:
    out: CreateSecurityConfigurationInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SecurityConfiguration" in data:
        out["security_configuration"] = data["SecurityConfiguration"]
    return out
