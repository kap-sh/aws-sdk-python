"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PortSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.variable_definition_list


class PortSet(TypedDict, closed=True):
    definition: NotRequired[
        "aws_sdk_network_firewall.types.variable_definition_list.VariableDefinitionList"
    ]
    """<p>The set of port ranges. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PortSet) -> dict:
    out: dict = {}
    if "definition" in value:
        import aws_sdk_network_firewall.types.variable_definition_list

        out["Definition"] = (
            aws_sdk_network_firewall.types.variable_definition_list.serialize_aws_json_1_0(
                value["definition"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PortSet:
    out: PortSet = {}  # type: ignore[typeddict-item]
    if "Definition" in data:
        import aws_sdk_network_firewall.types.variable_definition_list

        out["definition"] = (
            aws_sdk_network_firewall.types.variable_definition_list.deserialize_aws_json_1_0(
                data["Definition"]
            )
        )
    return out
