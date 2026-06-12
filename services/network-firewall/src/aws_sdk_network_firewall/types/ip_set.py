"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPSet``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.variable_definition_list


class IPSet(TypedDict):
    definition: (
        "aws_sdk_network_firewall.types.variable_definition_list.VariableDefinitionList"
    )
    """<p>The list of IP addresses and address ranges, in CIDR notation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IPSet) -> dict:
    out: dict = {}
    import aws_sdk_network_firewall.types.variable_definition_list

    out["Definition"] = (
        aws_sdk_network_firewall.types.variable_definition_list.serialize_aws_json_1_0(
            value["definition"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IPSet:
    out: IPSet = {}  # type: ignore[typeddict-item]
    if "Definition" in data:
        import aws_sdk_network_firewall.types.variable_definition_list

        out["definition"] = (
            aws_sdk_network_firewall.types.variable_definition_list.deserialize_aws_json_1_0(
                data["Definition"]
            )
        )
    else:
        raise DeserializationError("IPSet.definition required")
    return out
