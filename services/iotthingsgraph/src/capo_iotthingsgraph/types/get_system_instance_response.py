"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetSystemInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.system_instance_description


class GetSystemInstanceResponse(TypedDict, closed=True):
    description: NotRequired[
        "capo_iotthingsgraph.types.system_instance_description.SystemInstanceDescription"
    ]
    """<p>An object that describes the system instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSystemInstanceResponse) -> dict:
    out: dict = {}
    if "description" in value:
        import capo_iotthingsgraph.types.system_instance_description

        out["description"] = (
            capo_iotthingsgraph.types.system_instance_description.serialize_aws_json_1_1(
                value["description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSystemInstanceResponse:
    out: GetSystemInstanceResponse = {}  # type: ignore[typeddict-item]
    if "description" in data:
        import capo_iotthingsgraph.types.system_instance_description

        out["description"] = (
            capo_iotthingsgraph.types.system_instance_description.deserialize_aws_json_1_1(
                data["description"]
            )
        )
    return out
