"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostSupportedInstanceTypesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.instance_type_list_definition
    import aws_sdk_outposts.types.token


class GetOutpostSupportedInstanceTypesOutput(TypedDict):
    instance_types: NotRequired[
        "aws_sdk_outposts.types.instance_type_list_definition.InstanceTypeListDefinition"
    ]
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostSupportedInstanceTypesOutput) -> dict:
    out: dict = {}
    if "instance_types" in value:
        import aws_sdk_outposts.types.instance_type_list_definition

        out["InstanceTypes"] = (
            aws_sdk_outposts.types.instance_type_list_definition.serialize_json(
                value["instance_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetOutpostSupportedInstanceTypesOutput:
    out: GetOutpostSupportedInstanceTypesOutput = {}  # type: ignore[typeddict-item]
    if "InstanceTypes" in data:
        import aws_sdk_outposts.types.instance_type_list_definition

        out["instance_types"] = (
            aws_sdk_outposts.types.instance_type_list_definition.deserialize_json(
                data["InstanceTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
