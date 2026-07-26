"""Generated from Smithy shape ``com.amazonaws.glue#CreateUsageProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.name_string
    import capo_glue.types.profile_configuration
    import capo_glue.types.tags_map


class CreateUsageProfileRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the usage profile.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the usage profile.</p>"""
    configuration: "capo_glue.types.profile_configuration.ProfileConfiguration"
    """<p>A <code>ProfileConfiguration</code> object specifying the job and session values for the profile.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>A list of tags applied to the usage profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUsageProfileRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_glue.types.profile_configuration

    out["Configuration"] = capo_glue.types.profile_configuration.serialize_aws_json_1_1(
        value["configuration"]
    )
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUsageProfileRequest:
    out: CreateUsageProfileRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateUsageProfileRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Configuration" in data:
        import capo_glue.types.profile_configuration

        out["configuration"] = (
            capo_glue.types.profile_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("CreateUsageProfileRequest.configuration required")
    if "Tags" in data:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
