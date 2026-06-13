"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentBindingPropertiesValueProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.predicate_list


class ComponentBindingPropertiesValueProperties(TypedDict):
    model: NotRequired["str"]
    """<p>An Amplify DataStore model.</p>"""
    field: NotRequired["str"]
    """<p>The field to bind the data to.</p>"""
    predicates: NotRequired[
        "aws_sdk_amplifyuibuilder.types.predicate_list.PredicateList"
    ]
    """<p>A list of predicates for binding a component's properties to data.</p>"""
    user_attribute: NotRequired["str"]
    """<p>An authenticated user attribute.</p>"""
    bucket: NotRequired["str"]
    """<p>An Amazon S3 bucket.</p>"""
    key: NotRequired["str"]
    """<p>The storage key for an Amazon S3 bucket.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value to assign to the property.</p>"""
    slot_name: NotRequired["str"]
    """<p>The name of a component slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentBindingPropertiesValueProperties) -> dict:
    out: dict = {}
    if "model" in value:
        out["model"] = value["model"]
    if "field" in value:
        out["field"] = value["field"]
    if "predicates" in value:
        import aws_sdk_amplifyuibuilder.types.predicate_list

        out["predicates"] = (
            aws_sdk_amplifyuibuilder.types.predicate_list.serialize_json(
                value["predicates"]
            )
        )
    if "user_attribute" in value:
        out["userAttribute"] = value["user_attribute"]
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key" in value:
        out["key"] = value["key"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "slot_name" in value:
        out["slotName"] = value["slot_name"]
    return out


def deserialize_json(data: dict) -> ComponentBindingPropertiesValueProperties:
    out: ComponentBindingPropertiesValueProperties = {}  # type: ignore[typeddict-item]
    if "model" in data:
        out["model"] = data["model"]
    if "field" in data:
        out["field"] = data["field"]
    if "predicates" in data:
        import aws_sdk_amplifyuibuilder.types.predicate_list

        out["predicates"] = (
            aws_sdk_amplifyuibuilder.types.predicate_list.deserialize_json(
                data["predicates"]
            )
        )
    if "userAttribute" in data:
        out["user_attribute"] = data["userAttribute"]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    if "key" in data:
        out["key"] = data["key"]
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    if "slotName" in data:
        out["slot_name"] = data["slotName"]
    return out
