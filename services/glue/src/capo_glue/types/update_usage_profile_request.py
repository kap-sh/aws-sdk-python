"""Generated from Smithy shape ``com.amazonaws.glue#UpdateUsageProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.name_string
    import capo_glue.types.profile_configuration


class UpdateUsageProfileRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the usage profile.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the usage profile.</p>"""
    configuration: "capo_glue.types.profile_configuration.ProfileConfiguration"
    """<p>A <code>ProfileConfiguration</code> object specifying the job and session values for the profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUsageProfileRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_glue.types.profile_configuration

    out["Configuration"] = capo_glue.types.profile_configuration.serialize_aws_json_1_1(
        value["configuration"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUsageProfileRequest:
    out: UpdateUsageProfileRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateUsageProfileRequest.name required")
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
        raise DeserializationError("UpdateUsageProfileRequest.configuration required")
    return out
