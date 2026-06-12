"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateEntitlementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.app_visibility
    import aws_sdk_appstream.types.description
    import aws_sdk_appstream.types.entitlement_attribute_list
    import aws_sdk_appstream.types.name


class UpdateEntitlementRequest(TypedDict):
    name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the entitlement.</p>"""
    stack_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the stack with which the entitlement is associated.</p>"""
    description: NotRequired["aws_sdk_appstream.types.description.Description"]
    """<p>The description of the entitlement.</p>"""
    app_visibility: NotRequired["aws_sdk_appstream.types.app_visibility.AppVisibility"]
    """<p>Specifies whether all or only selected apps are entitled.</p>"""
    attributes: NotRequired[
        "aws_sdk_appstream.types.entitlement_attribute_list.EntitlementAttributeList"
    ]
    """<p>The attributes of the entitlement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEntitlementRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "app_visibility" in value:
        import aws_sdk_appstream.types.app_visibility

        out["AppVisibility"] = (
            aws_sdk_appstream.types.app_visibility.serialize_aws_json_1_1(
                value["app_visibility"]
            )
        )
    if "attributes" in value:
        import aws_sdk_appstream.types.entitlement_attribute_list

        out["Attributes"] = (
            aws_sdk_appstream.types.entitlement_attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEntitlementRequest:
    out: UpdateEntitlementRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "AppVisibility" in data:
        import aws_sdk_appstream.types.app_visibility

        out["app_visibility"] = (
            aws_sdk_appstream.types.app_visibility.deserialize_aws_json_1_1(
                data["AppVisibility"]
            )
        )
    if "Attributes" in data:
        import aws_sdk_appstream.types.entitlement_attribute_list

        out["attributes"] = (
            aws_sdk_appstream.types.entitlement_attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    return out
