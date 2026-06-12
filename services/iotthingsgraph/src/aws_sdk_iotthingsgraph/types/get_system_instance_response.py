"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetSystemInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_instance_description


class GetSystemInstanceResponse(TypedDict):
    description: NotRequired[
        "aws_sdk_iotthingsgraph.types.system_instance_description.SystemInstanceDescription"
    ]
    """<p>An object that describes the system instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSystemInstanceResponse) -> dict:
    out: dict = {}
    if "description" in value:
        import aws_sdk_iotthingsgraph.types.system_instance_description

        out["description"] = (
            aws_sdk_iotthingsgraph.types.system_instance_description.serialize_aws_json_1_1(
                value["description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSystemInstanceResponse:
    out: GetSystemInstanceResponse = {}  # type: ignore[typeddict-item]
    if "description" in data:
        import aws_sdk_iotthingsgraph.types.system_instance_description

        out["description"] = (
            aws_sdk_iotthingsgraph.types.system_instance_description.deserialize_aws_json_1_1(
                data["description"]
            )
        )
    return out
