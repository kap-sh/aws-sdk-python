"""Generated from Smithy shape ``com.amazonaws.appstream#Entitlement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.app_visibility
    import aws_sdk_appstream.types.description
    import aws_sdk_appstream.types.entitlement_attribute_list
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.timestamp


class Entitlement(TypedDict, closed=True):
    name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the entitlement.</p>"""
    stack_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the stack with which the entitlement is associated.</p>"""
    description: NotRequired["aws_sdk_appstream.types.description.Description"]
    """<p>The description of the entitlement.</p>"""
    app_visibility: NotRequired["aws_sdk_appstream.types.app_visibility.AppVisibility"]
    """<p>Specifies whether all or selected apps are entitled.</p>"""
    attributes: NotRequired[
        "aws_sdk_appstream.types.entitlement_attribute_list.EntitlementAttributeList"
    ]
    """<p>The attributes of the entitlement.</p>"""
    created_time: NotRequired["aws_sdk_appstream.types.timestamp.Timestamp"]
    """<p>The time when the entitlement was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_appstream.types.timestamp.Timestamp"]
    """<p>The time when the entitlement was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entitlement) -> dict:
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
    if "created_time" in value:
        import aws_sdk_appstream.types.timestamp

        out["CreatedTime"] = aws_sdk_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_appstream.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_appstream.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Entitlement:
    out: Entitlement = {}  # type: ignore[typeddict-item]
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
    if "CreatedTime" in data:
        import aws_sdk_appstream.types.timestamp

        out["created_time"] = (
            aws_sdk_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_appstream.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
