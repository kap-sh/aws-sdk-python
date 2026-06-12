"""Generated from Smithy shape ``com.amazonaws.directoryservice#Computer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.attributes
    import aws_sdk_directory_service.types.computer_name
    import aws_sdk_directory_service.types.sid


class Computer(TypedDict):
    computer_id: NotRequired["aws_sdk_directory_service.types.sid.SID"]
    """<p>The identifier of the computer.</p>"""
    computer_name: NotRequired[
        "aws_sdk_directory_service.types.computer_name.ComputerName"
    ]
    """<p>The computer name.</p>"""
    computer_attributes: NotRequired[
        "aws_sdk_directory_service.types.attributes.Attributes"
    ]
    """<p>An array of <a>Attribute</a> objects containing the LDAP attributes that belong to the computer account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Computer) -> dict:
    out: dict = {}
    if "computer_id" in value:
        out["ComputerId"] = value["computer_id"]
    if "computer_name" in value:
        out["ComputerName"] = value["computer_name"]
    if "computer_attributes" in value:
        import aws_sdk_directory_service.types.attributes

        out["ComputerAttributes"] = (
            aws_sdk_directory_service.types.attributes.serialize_aws_json_1_1(
                value["computer_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Computer:
    out: Computer = {}  # type: ignore[typeddict-item]
    if "ComputerId" in data:
        out["computer_id"] = data["ComputerId"]
    if "ComputerName" in data:
        out["computer_name"] = data["ComputerName"]
    if "ComputerAttributes" in data:
        import aws_sdk_directory_service.types.attributes

        out["computer_attributes"] = (
            aws_sdk_directory_service.types.attributes.deserialize_aws_json_1_1(
                data["ComputerAttributes"]
            )
        )
    return out
