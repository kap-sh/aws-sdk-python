"""Generated from Smithy shape ``com.amazonaws.iam#OrderedOrganizationPolicyType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.simulation_policy_list_type


class OrderedOrganizationPolicyType(TypedDict, closed=True):
    service_control_policy_input_list: NotRequired[
        "capo_iam.types.simulation_policy_list_type.SimulationPolicyListType"
    ]
    """<p>A list of SCP documents that apply at this level of the Organizations hierarchy. Each document is specified as a string containing the complete, valid JSON text of an SCP.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderedOrganizationPolicyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "service_control_policy_input_list" in value:
        import capo_iam.types.simulation_policy_list_type

        capo_iam.types.simulation_policy_list_type.serialize_query(
            value["service_control_policy_input_list"],
            pairs,
            f"{key_prefix}ServiceControlPolicyInputList",
        )


def deserialize_query(el: Element) -> OrderedOrganizationPolicyType:
    out: OrderedOrganizationPolicyType = {}  # type: ignore[typeddict-item]
    child_service_control_policy_input_list = el.find("ServiceControlPolicyInputList")
    if child_service_control_policy_input_list is not None:
        import capo_iam.types.simulation_policy_list_type

        out["service_control_policy_input_list"] = (
            capo_iam.types.simulation_policy_list_type.deserialize_query(
                child_service_control_policy_input_list
            )
        )
    return out
