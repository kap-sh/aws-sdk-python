"""Generated from Smithy shape ``com.amazonaws.athena#Database``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.description_string
    import capo_athena.types.name_string
    import capo_athena.types.parameters_map


class Database(TypedDict, closed=True):
    name: "capo_athena.types.name_string.NameString"
    """<p>The name of the database.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>An optional description of the database.</p>"""
    parameters: NotRequired["capo_athena.types.parameters_map.ParametersMap"]
    """<p>A set of custom key/value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Database) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "parameters" in value:
        import capo_athena.types.parameters_map

        out["Parameters"] = capo_athena.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Database:
    out: Database = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Database.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Parameters" in data:
        import capo_athena.types.parameters_map

        out["parameters"] = capo_athena.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    return out
