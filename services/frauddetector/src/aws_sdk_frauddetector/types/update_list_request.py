"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.elements_list
    import aws_sdk_frauddetector.types.list_update_mode
    import aws_sdk_frauddetector.types.no_dash_identifier
    import aws_sdk_frauddetector.types.variable_type


class UpdateListRequest(TypedDict):
    name: "aws_sdk_frauddetector.types.no_dash_identifier.noDashIdentifier"
    """<p> The name of the list to update. </p>"""
    elements: NotRequired["aws_sdk_frauddetector.types.elements_list.ElementsList"]
    """<p> One or more list elements to add or replace. If you are providing the elements, make sure to specify the <code>updateMode</code> to use. </p> <p>If you are deleting all elements from the list, use <code>REPLACE</code> for the <code>updateMode</code> and provide an empty list (0 elements).</p>"""
    description: NotRequired["aws_sdk_frauddetector.types.description.description"]
    """<p> The new description. </p>"""
    update_mode: NotRequired[
        "aws_sdk_frauddetector.types.list_update_mode.ListUpdateMode"
    ]
    """<p> The update mode (type). </p> <ul> <li> <p>Use <code>APPEND</code> if you are adding elements to the list.</p> </li> <li> <p>Use <code>REPLACE</code> if you replacing existing elements in the list.</p> </li> <li> <p>Use <code>REMOVE</code> if you are removing elements from the list.</p> </li> </ul>"""
    variable_type: NotRequired["aws_sdk_frauddetector.types.variable_type.variableType"]
    """<p> The variable type you want to assign to the list. </p> <note> <p>You cannot update a variable type of a list that already has a variable type assigned to it. You can assign a variable type to a list only if the list does not already have a variable type.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateListRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "elements" in value:
        import aws_sdk_frauddetector.types.elements_list

        out["elements"] = (
            aws_sdk_frauddetector.types.elements_list.serialize_aws_json_1_1(
                value["elements"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "update_mode" in value:
        import aws_sdk_frauddetector.types.list_update_mode

        out["updateMode"] = (
            aws_sdk_frauddetector.types.list_update_mode.serialize_aws_json_1_1(
                value["update_mode"]
            )
        )
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateListRequest:
    out: UpdateListRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateListRequest.name required")
    if "elements" in data:
        import aws_sdk_frauddetector.types.elements_list

        out["elements"] = (
            aws_sdk_frauddetector.types.elements_list.deserialize_aws_json_1_1(
                data["elements"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "updateMode" in data:
        import aws_sdk_frauddetector.types.list_update_mode

        out["update_mode"] = (
            aws_sdk_frauddetector.types.list_update_mode.deserialize_aws_json_1_1(
                data["updateMode"]
            )
        )
    if "variableType" in data:
        out["variable_type"] = data["variableType"]
    return out
