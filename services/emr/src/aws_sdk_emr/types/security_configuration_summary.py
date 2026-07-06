"""Generated from Smithy shape ``com.amazonaws.emr#SecurityConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.xml_string


class SecurityConfigurationSummary(TypedDict, closed=True):
    name: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The name of the security configuration.</p>"""
    creation_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time the security configuration was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityConfigurationSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "creation_date_time" in value:
        import aws_sdk_emr.types.date

        out["CreationDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SecurityConfigurationSummary:
    out: SecurityConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreationDateTime" in data:
        import aws_sdk_emr.types.date

        out["creation_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreationDateTime"]
        )
    return out
