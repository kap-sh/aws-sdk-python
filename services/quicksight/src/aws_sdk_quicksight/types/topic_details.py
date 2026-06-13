"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.datasets
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.resource_name
    import aws_sdk_quicksight.types.topic_config_options
    import aws_sdk_quicksight.types.topic_user_experience_version


class TopicDetails(TypedDict):
    name: NotRequired["aws_sdk_quicksight.types.resource_name.ResourceName"]
    """<p>The name of the topic.</p>"""
    description: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The description of the topic.</p>"""
    user_experience_version: NotRequired[
        "aws_sdk_quicksight.types.topic_user_experience_version.TopicUserExperienceVersion"
    ]
    """<p>The user experience version of a topic.</p>"""
    data_sets: NotRequired["aws_sdk_quicksight.types.datasets.Datasets"]
    """<p>The data sets that the topic is associated with.</p>"""
    config_options: NotRequired[
        "aws_sdk_quicksight.types.topic_config_options.TopicConfigOptions"
    ]
    """<p>Configuration options for a <code>Topic</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "user_experience_version" in value:
        import aws_sdk_quicksight.types.topic_user_experience_version

        out["UserExperienceVersion"] = (
            aws_sdk_quicksight.types.topic_user_experience_version.serialize_json(
                value["user_experience_version"]
            )
        )
    if "data_sets" in value:
        import aws_sdk_quicksight.types.datasets

        out["DataSets"] = aws_sdk_quicksight.types.datasets.serialize_json(
            value["data_sets"]
        )
    if "config_options" in value:
        import aws_sdk_quicksight.types.topic_config_options

        out["ConfigOptions"] = (
            aws_sdk_quicksight.types.topic_config_options.serialize_json(
                value["config_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicDetails:
    out: TopicDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "UserExperienceVersion" in data:
        import aws_sdk_quicksight.types.topic_user_experience_version

        out["user_experience_version"] = (
            aws_sdk_quicksight.types.topic_user_experience_version.deserialize_json(
                data["UserExperienceVersion"]
            )
        )
    if "DataSets" in data:
        import aws_sdk_quicksight.types.datasets

        out["data_sets"] = aws_sdk_quicksight.types.datasets.deserialize_json(
            data["DataSets"]
        )
    if "ConfigOptions" in data:
        import aws_sdk_quicksight.types.topic_config_options

        out["config_options"] = (
            aws_sdk_quicksight.types.topic_config_options.deserialize_json(
                data["ConfigOptions"]
            )
        )
    return out
