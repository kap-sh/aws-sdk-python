"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.policy_attribute_descriptions
    import aws_sdk_elastic_load_balancing.types.policy_name
    import aws_sdk_elastic_load_balancing.types.policy_type_name


class PolicyDescription(TypedDict, closed=True):
    policy_name: NotRequired[
        "aws_sdk_elastic_load_balancing.types.policy_name.PolicyName"
    ]
    """<p>The name of the policy.</p>"""
    policy_type_name: NotRequired[
        "aws_sdk_elastic_load_balancing.types.policy_type_name.PolicyTypeName"
    ]
    """<p>The name of the policy type.</p>"""
    policy_attribute_descriptions: NotRequired[
        "aws_sdk_elastic_load_balancing.types.policy_attribute_descriptions.PolicyAttributeDescriptions"
    ]
    """<p>The policy attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy_name" in value:
        pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    if "policy_type_name" in value:
        pairs.append((f"{prefix}.PolicyTypeName", str(value["policy_type_name"])))
    if "policy_attribute_descriptions" in value:
        import aws_sdk_elastic_load_balancing.types.policy_attribute_descriptions

        aws_sdk_elastic_load_balancing.types.policy_attribute_descriptions.serialize_query(
            value["policy_attribute_descriptions"],
            pairs,
            f"{prefix}.PolicyAttributeDescriptions",
        )


def deserialize_query(el: Element) -> PolicyDescription:
    out: PolicyDescription = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_policy_type_name = el.find("PolicyTypeName")
    if child_policy_type_name is not None:
        out["policy_type_name"] = str(child_policy_type_name.text or "")
    child_policy_attribute_descriptions = el.find("PolicyAttributeDescriptions")
    if child_policy_attribute_descriptions is not None:
        import aws_sdk_elastic_load_balancing.types.policy_attribute_descriptions

        out["policy_attribute_descriptions"] = (
            aws_sdk_elastic_load_balancing.types.policy_attribute_descriptions.deserialize_query(
                child_policy_attribute_descriptions
            )
        )
    return out
