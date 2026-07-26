"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostSupportedInstanceTypesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.instance_type_list_definition
    import capo_outposts.types.token


class GetOutpostSupportedInstanceTypesOutput(TypedDict, closed=True):
    instance_types: NotRequired[
        "capo_outposts.types.instance_type_list_definition.InstanceTypeListDefinition"
    ]
    next_token: NotRequired["capo_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostSupportedInstanceTypesOutput) -> dict:
    out: dict = {}
    if "instance_types" in value:
        import capo_outposts.types.instance_type_list_definition

        out["InstanceTypes"] = (
            capo_outposts.types.instance_type_list_definition.serialize_json(
                value["instance_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetOutpostSupportedInstanceTypesOutput:
    out: GetOutpostSupportedInstanceTypesOutput = {}  # type: ignore[typeddict-item]
    if "InstanceTypes" in data:
        import capo_outposts.types.instance_type_list_definition

        out["instance_types"] = (
            capo_outposts.types.instance_type_list_definition.deserialize_json(
                data["InstanceTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
