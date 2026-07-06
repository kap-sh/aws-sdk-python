"""Generated from Smithy shape ``com.amazonaws.outposts#ListOrderableInstanceTypesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.detailed_instance_type_list_definition
    import aws_sdk_outposts.types.token


class ListOrderableInstanceTypesOutput(TypedDict, closed=True):
    instance_types: NotRequired[
        "aws_sdk_outposts.types.detailed_instance_type_list_definition.DetailedInstanceTypeListDefinition"
    ]
    """<p>Information about the instance types that can be ordered for the Outpost.</p>"""
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrderableInstanceTypesOutput) -> dict:
    out: dict = {}
    if "instance_types" in value:
        import aws_sdk_outposts.types.detailed_instance_type_list_definition

        out["InstanceTypes"] = (
            aws_sdk_outposts.types.detailed_instance_type_list_definition.serialize_json(
                value["instance_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOrderableInstanceTypesOutput:
    out: ListOrderableInstanceTypesOutput = {}  # type: ignore[typeddict-item]
    if "InstanceTypes" in data:
        import aws_sdk_outposts.types.detailed_instance_type_list_definition

        out["instance_types"] = (
            aws_sdk_outposts.types.detailed_instance_type_list_definition.deserialize_json(
                data["InstanceTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
