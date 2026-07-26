"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyTypeDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.description
    import capo_elastic_load_balancing.types.policy_attribute_type_descriptions
    import capo_elastic_load_balancing.types.policy_type_name


class PolicyTypeDescription(TypedDict, closed=True):
    policy_type_name: NotRequired[
        "capo_elastic_load_balancing.types.policy_type_name.PolicyTypeName"
    ]
    """<p>The name of the policy type.</p>"""
    description: NotRequired[
        "capo_elastic_load_balancing.types.description.Description"
    ]
    """<p>A description of the policy type.</p>"""
    policy_attribute_type_descriptions: NotRequired[
        "capo_elastic_load_balancing.types.policy_attribute_type_descriptions.PolicyAttributeTypeDescriptions"
    ]
    """<p>The description of the policy attributes associated with the policies defined by Elastic Load Balancing.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyTypeDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy_type_name" in value:
        pairs.append((f"{prefix}.PolicyTypeName", str(value["policy_type_name"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "policy_attribute_type_descriptions" in value:
        import capo_elastic_load_balancing.types.policy_attribute_type_descriptions

        capo_elastic_load_balancing.types.policy_attribute_type_descriptions.serialize_query(
            value["policy_attribute_type_descriptions"],
            pairs,
            f"{prefix}.PolicyAttributeTypeDescriptions",
        )


def deserialize_query(el: Element) -> PolicyTypeDescription:
    out: PolicyTypeDescription = {}  # type: ignore[typeddict-item]
    child_policy_type_name = el.find("PolicyTypeName")
    if child_policy_type_name is not None:
        out["policy_type_name"] = str(child_policy_type_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_policy_attribute_type_descriptions = el.find(
        "PolicyAttributeTypeDescriptions"
    )
    if child_policy_attribute_type_descriptions is not None:
        import capo_elastic_load_balancing.types.policy_attribute_type_descriptions

        out["policy_attribute_type_descriptions"] = (
            capo_elastic_load_balancing.types.policy_attribute_type_descriptions.deserialize_query(
                child_policy_attribute_type_descriptions
            )
        )
    return out
