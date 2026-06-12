"""Generated from Smithy shape ``com.amazonaws.emr#StudioSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.auth_mode
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.xml_string_max_len256


class StudioSummary(TypedDict):
    studio_id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the Amazon EMR Studio.</p>"""
    name: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the Amazon EMR Studio.</p>"""
    vpc_id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the Virtual Private Cloud (Amazon VPC) associated with the Amazon EMR Studio.</p>"""
    description: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The detailed description of the Amazon EMR Studio.</p>"""
    url: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The unique access URL of the Amazon EMR Studio.</p>"""
    auth_mode: NotRequired["aws_sdk_emr.types.auth_mode.AuthMode"]
    """<p>Specifies whether the Studio authenticates users using IAM or IAM Identity Center.</p>"""
    creation_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The time when the Amazon EMR Studio was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StudioSummary) -> dict:
    out: dict = {}
    if "studio_id" in value:
        out["StudioId"] = value["studio_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "url" in value:
        out["Url"] = value["url"]
    if "auth_mode" in value:
        import aws_sdk_emr.types.auth_mode

        out["AuthMode"] = aws_sdk_emr.types.auth_mode.serialize_aws_json_1_1(
            value["auth_mode"]
        )
    if "creation_time" in value:
        import aws_sdk_emr.types.date

        out["CreationTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StudioSummary:
    out: StudioSummary = {}  # type: ignore[typeddict-item]
    if "StudioId" in data:
        out["studio_id"] = data["StudioId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Url" in data:
        out["url"] = data["Url"]
    if "AuthMode" in data:
        import aws_sdk_emr.types.auth_mode

        out["auth_mode"] = aws_sdk_emr.types.auth_mode.deserialize_aws_json_1_1(
            data["AuthMode"]
        )
    if "CreationTime" in data:
        import aws_sdk_emr.types.date

        out["creation_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
