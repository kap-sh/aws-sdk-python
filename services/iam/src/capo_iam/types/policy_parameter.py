"""Generated from Smithy shape ``com.amazonaws.iam#PolicyParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy_parameter_name_type
    import capo_iam.types.policy_parameter_type_enum
    import capo_iam.types.policy_parameter_values_list_type


class PolicyParameter(TypedDict, closed=True):
    name: NotRequired[
        "capo_iam.types.policy_parameter_name_type.policyParameterNameType"
    ]
    """<p>The name of the policy parameter.</p>"""
    values: NotRequired[
        "capo_iam.types.policy_parameter_values_list_type.policyParameterValuesListType"
    ]
    """<p>The allowed values for the policy parameter.</p>"""
    type: NotRequired[
        "capo_iam.types.policy_parameter_type_enum.PolicyParameterTypeEnum"
    ]
    """<p>The data type of the policy parameter value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyParameter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "values" in value:
        import capo_iam.types.policy_parameter_values_list_type

        capo_iam.types.policy_parameter_values_list_type.serialize_query(
            value["values"], pairs, f"{prefix}.Values"
        )
    if "type" in value:
        import capo_iam.types.policy_parameter_type_enum

        capo_iam.types.policy_parameter_type_enum.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )


def deserialize_query(el: Element) -> PolicyParameter:
    out: PolicyParameter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import capo_iam.types.policy_parameter_values_list_type

        out["values"] = (
            capo_iam.types.policy_parameter_values_list_type.deserialize_query(
                child_values
            )
        )
    child_type = el.find("Type")
    if child_type is not None:
        import capo_iam.types.policy_parameter_type_enum

        out["type"] = capo_iam.types.policy_parameter_type_enum.deserialize_query(
            child_type
        )
    return out
