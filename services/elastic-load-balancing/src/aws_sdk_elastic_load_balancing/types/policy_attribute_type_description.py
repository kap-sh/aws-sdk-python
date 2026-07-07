"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyAttributeTypeDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.attribute_name
    import aws_sdk_elastic_load_balancing.types.attribute_type
    import aws_sdk_elastic_load_balancing.types.cardinality
    import aws_sdk_elastic_load_balancing.types.default_value
    import aws_sdk_elastic_load_balancing.types.description


class PolicyAttributeTypeDescription(TypedDict, closed=True):
    attribute_name: NotRequired[
        "aws_sdk_elastic_load_balancing.types.attribute_name.AttributeName"
    ]
    """<p>The name of the attribute.</p>"""
    attribute_type: NotRequired[
        "aws_sdk_elastic_load_balancing.types.attribute_type.AttributeType"
    ]
    """<p>The type of the attribute. For example, <code>Boolean</code> or <code>Integer</code>.</p>"""
    description: NotRequired[
        "aws_sdk_elastic_load_balancing.types.description.Description"
    ]
    """<p>A description of the attribute.</p>"""
    default_value: NotRequired[
        "aws_sdk_elastic_load_balancing.types.default_value.DefaultValue"
    ]
    """<p>The default value of the attribute, if applicable.</p>"""
    cardinality: NotRequired[
        "aws_sdk_elastic_load_balancing.types.cardinality.Cardinality"
    ]
    """<p>The cardinality of the attribute.</p> <p>Valid values:</p> <ul> <li> <p>ONE(1) : Single value required</p> </li> <li> <p>ZERO_OR_ONE(0..1) : Up to one value is allowed</p> </li> <li> <p>ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed</p> </li> <li> <p>ONE_OR_MORE(1..*0) : Required. Multiple values are allowed</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyAttributeTypeDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute_name" in value:
        pairs.append((f"{prefix}.AttributeName", str(value["attribute_name"])))
    if "attribute_type" in value:
        pairs.append((f"{prefix}.AttributeType", str(value["attribute_type"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "default_value" in value:
        pairs.append((f"{prefix}.DefaultValue", str(value["default_value"])))
    if "cardinality" in value:
        pairs.append((f"{prefix}.Cardinality", str(value["cardinality"])))


def deserialize_query(el: Element) -> PolicyAttributeTypeDescription:
    out: PolicyAttributeTypeDescription = {}  # type: ignore[typeddict-item]
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    child_attribute_type = el.find("AttributeType")
    if child_attribute_type is not None:
        out["attribute_type"] = str(child_attribute_type.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_cardinality = el.find("Cardinality")
    if child_cardinality is not None:
        out["cardinality"] = str(child_cardinality.text or "")
    return out
