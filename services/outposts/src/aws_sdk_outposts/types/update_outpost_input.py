"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateOutpostInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.outpost_description
    import aws_sdk_outposts.types.outpost_id
    import aws_sdk_outposts.types.outpost_name
    import aws_sdk_outposts.types.supported_hardware_type


class UpdateOutpostInput(TypedDict):
    outpost_id: "aws_sdk_outposts.types.outpost_id.OutpostId"
    """<p> The ID or ARN of the Outpost. </p>"""
    name: NotRequired["aws_sdk_outposts.types.outpost_name.OutpostName"]
    description: NotRequired[
        "aws_sdk_outposts.types.outpost_description.OutpostDescription"
    ]
    supported_hardware_type: NotRequired[
        "aws_sdk_outposts.types.supported_hardware_type.SupportedHardwareType"
    ]
    """<p> The type of hardware for this Outpost. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutpostInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "supported_hardware_type" in value:
        import aws_sdk_outposts.types.supported_hardware_type

        out["SupportedHardwareType"] = (
            aws_sdk_outposts.types.supported_hardware_type.serialize_json(
                value["supported_hardware_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateOutpostInput:
    out: UpdateOutpostInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "SupportedHardwareType" in data:
        import aws_sdk_outposts.types.supported_hardware_type

        out["supported_hardware_type"] = (
            aws_sdk_outposts.types.supported_hardware_type.deserialize_json(
                data["SupportedHardwareType"]
            )
        )
    return out
