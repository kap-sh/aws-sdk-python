"""Generated from Smithy shape ``com.amazonaws.cloudformation#PropertyDifference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.difference_type
    import capo_cloudformation.types.property_path
    import capo_cloudformation.types.property_value


class PropertyDifference(TypedDict, closed=True):
    property_path: NotRequired["capo_cloudformation.types.property_path.PropertyPath"]
    """<p>The fully-qualified path to the resource property.</p>"""
    expected_value: NotRequired[
        "capo_cloudformation.types.property_value.PropertyValue"
    ]
    """<p>The expected property value of the resource property, as defined in the stack template and any values specified as template parameters.</p>"""
    actual_value: NotRequired["capo_cloudformation.types.property_value.PropertyValue"]
    """<p>The actual property value of the resource property.</p>"""
    difference_type: NotRequired[
        "capo_cloudformation.types.difference_type.DifferenceType"
    ]
    """<p>The type of property difference.</p> <ul> <li> <p> <code>ADD</code>: A value has been added to a resource property that's an array or list data type.</p> </li> <li> <p> <code>REMOVE</code>: The property has been removed from the current resource configuration.</p> </li> <li> <p> <code>NOT_EQUAL</code>: The current property value differs from its expected value (as defined in the stack template and any values specified as template parameters).</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PropertyDifference, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "property_path" in value:
        pairs.append((f"{prefix}.PropertyPath", str(value["property_path"])))
    if "expected_value" in value:
        pairs.append((f"{prefix}.ExpectedValue", str(value["expected_value"])))
    if "actual_value" in value:
        pairs.append((f"{prefix}.ActualValue", str(value["actual_value"])))
    if "difference_type" in value:
        import capo_cloudformation.types.difference_type

        capo_cloudformation.types.difference_type.serialize_query(
            value["difference_type"], pairs, f"{prefix}.DifferenceType"
        )


def deserialize_query(el: Element) -> PropertyDifference:
    out: PropertyDifference = {}  # type: ignore[typeddict-item]
    child_property_path = el.find("PropertyPath")
    if child_property_path is not None:
        out["property_path"] = str(child_property_path.text or "")
    child_expected_value = el.find("ExpectedValue")
    if child_expected_value is not None:
        out["expected_value"] = str(child_expected_value.text or "")
    child_actual_value = el.find("ActualValue")
    if child_actual_value is not None:
        out["actual_value"] = str(child_actual_value.text or "")
    child_difference_type = el.find("DifferenceType")
    if child_difference_type is not None:
        import capo_cloudformation.types.difference_type

        out["difference_type"] = (
            capo_cloudformation.types.difference_type.deserialize_query(
                child_difference_type
            )
        )
    return out
