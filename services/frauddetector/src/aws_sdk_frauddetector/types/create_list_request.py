"""Generated from Smithy shape ``com.amazonaws.frauddetector#CreateListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.elements_list
    import aws_sdk_frauddetector.types.no_dash_identifier
    import aws_sdk_frauddetector.types.tag_list
    import aws_sdk_frauddetector.types.variable_type


class CreateListRequest(TypedDict):
    name: "aws_sdk_frauddetector.types.no_dash_identifier.noDashIdentifier"
    """<p> The name of the list. </p>"""
    elements: NotRequired["aws_sdk_frauddetector.types.elements_list.ElementsList"]
    r"""<p> The names of the elements, if providing. You can also create an empty list and add elements later using the <a href=\"https://docs.aws.amazon.com/frauddetector/latest/api/API_Updatelist.html\">UpdateList</a> API. </p>"""
    variable_type: NotRequired["aws_sdk_frauddetector.types.variable_type.variableType"]
    r"""<p> The variable type of the list. You can only assign the variable type with String data type. For more information, see <a href=\"https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types\">Variable types</a>. </p>"""
    description: NotRequired["aws_sdk_frauddetector.types.description.description"]
    """<p> The description of the list. </p>"""
    tags: NotRequired["aws_sdk_frauddetector.types.tag_list.tagList"]
    """<p> A collection of the key and value pairs. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateListRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "elements" in value:
        import aws_sdk_frauddetector.types.elements_list

        out["elements"] = (
            aws_sdk_frauddetector.types.elements_list.serialize_aws_json_1_1(
                value["elements"]
            )
        )
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateListRequest:
    out: CreateListRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateListRequest.name required")
    if "elements" in data:
        import aws_sdk_frauddetector.types.elements_list

        out["elements"] = (
            aws_sdk_frauddetector.types.elements_list.deserialize_aws_json_1_1(
                data["elements"]
            )
        )
    if "variableType" in data:
        out["variable_type"] = data["variableType"]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
