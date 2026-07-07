"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateCalculatedAttributeDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.conditions
    import aws_sdk_customer_profiles.types.display_name
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.sensitive_text
    import aws_sdk_customer_profiles.types.type_name


class UpdateCalculatedAttributeDefinitionRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    calculated_attribute_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the calculated attribute.</p>"""
    display_name: NotRequired[
        "aws_sdk_customer_profiles.types.display_name.displayName"
    ]
    """<p>The display name of the calculated attribute.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the calculated attribute.</p>"""
    conditions: NotRequired["aws_sdk_customer_profiles.types.conditions.Conditions"]
    """<p>The conditions including range, object count, and threshold for the calculated attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCalculatedAttributeDefinitionRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "conditions" in value:
        import aws_sdk_customer_profiles.types.conditions

        out["Conditions"] = aws_sdk_customer_profiles.types.conditions.serialize_json(
            value["conditions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCalculatedAttributeDefinitionRequest:
    out: UpdateCalculatedAttributeDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Conditions" in data:
        import aws_sdk_customer_profiles.types.conditions

        out["conditions"] = aws_sdk_customer_profiles.types.conditions.deserialize_json(
            data["Conditions"]
        )
    return out
