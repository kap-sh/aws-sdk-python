"""Generated from Smithy shape ``com.amazonaws.configservice#PutConfigurationRecorderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.configuration_recorder
    import capo_config_service.types.tags_list


class PutConfigurationRecorderRequest(TypedDict, closed=True):
    configuration_recorder: (
        "capo_config_service.types.configuration_recorder.ConfigurationRecorder"
    )
    """<p>An object for the configuration recorder. A configuration recorder records configuration changes for the resource types in scope.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>The tags for the customer managed configuration recorder. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutConfigurationRecorderRequest) -> dict:
    out: dict = {}
    import capo_config_service.types.configuration_recorder

    out["ConfigurationRecorder"] = (
        capo_config_service.types.configuration_recorder.serialize_aws_json_1_1(
            value["configuration_recorder"]
        )
    )
    if "tags" in value:
        import capo_config_service.types.tags_list

        out["Tags"] = capo_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConfigurationRecorderRequest:
    out: PutConfigurationRecorderRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecorder" in data:
        import capo_config_service.types.configuration_recorder

        out["configuration_recorder"] = (
            capo_config_service.types.configuration_recorder.deserialize_aws_json_1_1(
                data["ConfigurationRecorder"]
            )
        )
    else:
        raise DeserializationError(
            "PutConfigurationRecorderRequest.configuration_recorder required"
        )
    if "Tags" in data:
        import capo_config_service.types.tags_list

        out["tags"] = capo_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
