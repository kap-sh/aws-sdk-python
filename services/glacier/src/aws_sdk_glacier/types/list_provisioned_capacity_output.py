"""Generated from Smithy shape ``com.amazonaws.glacier#ListProvisionedCapacityOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.provisioned_capacity_list


class ListProvisionedCapacityOutput(TypedDict, closed=True):
    provisioned_capacity_list: NotRequired[
        "aws_sdk_glacier.types.provisioned_capacity_list.ProvisionedCapacityList"
    ]
    """<p>The response body contains the following JSON fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProvisionedCapacityOutput) -> dict:
    out: dict = {}
    if "provisioned_capacity_list" in value:
        import aws_sdk_glacier.types.provisioned_capacity_list

        out["ProvisionedCapacityList"] = (
            aws_sdk_glacier.types.provisioned_capacity_list.serialize_json(
                value["provisioned_capacity_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListProvisionedCapacityOutput:
    out: ListProvisionedCapacityOutput = {}  # type: ignore[typeddict-item]
    if "ProvisionedCapacityList" in data:
        import aws_sdk_glacier.types.provisioned_capacity_list

        out["provisioned_capacity_list"] = (
            aws_sdk_glacier.types.provisioned_capacity_list.deserialize_json(
                data["ProvisionedCapacityList"]
            )
        )
    return out
