"""Generated from Smithy shape ``com.amazonaws.emr#DescribeSecurityConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.date
    import capo_emr.types.string
    import capo_emr.types.xml_string


class DescribeSecurityConfigurationOutput(TypedDict, closed=True):
    name: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The name of the security configuration.</p>"""
    security_configuration: NotRequired["capo_emr.types.string.String"]
    """<p>The security configuration details in JSON format.</p>"""
    creation_date_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The date and time the security configuration was created</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSecurityConfigurationOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "creation_date_time" in value:
        import capo_emr.types.date

        out["CreationDateTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSecurityConfigurationOutput:
    out: DescribeSecurityConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SecurityConfiguration" in data:
        out["security_configuration"] = data["SecurityConfiguration"]
    if "CreationDateTime" in data:
        import capo_emr.types.date

        out["creation_date_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["CreationDateTime"]
        )
    return out
