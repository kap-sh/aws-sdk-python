"""Generated from Smithy shape ``com.amazonaws.glue#UsageProfileDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.timestamp_value


class UsageProfileDefinition(TypedDict, closed=True):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the usage profile.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the usage profile.</p>"""
    created_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time when the usage profile was created.</p>"""
    last_modified_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time when the usage profile was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageProfileDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_on" in value:
        import aws_sdk_glue.types.timestamp_value

        out["CreatedOn"] = aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["created_on"]
        )
    if "last_modified_on" in value:
        import aws_sdk_glue.types.timestamp_value

        out["LastModifiedOn"] = (
            aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
                value["last_modified_on"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UsageProfileDefinition:
    out: UsageProfileDefinition = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedOn" in data:
        import aws_sdk_glue.types.timestamp_value

        out["created_on"] = aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["CreatedOn"]
        )
    if "LastModifiedOn" in data:
        import aws_sdk_glue.types.timestamp_value

        out["last_modified_on"] = (
            aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["LastModifiedOn"]
            )
        )
    return out
