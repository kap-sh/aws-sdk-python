"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeleteTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configuration_id_list
    import aws_sdk_application_discovery_service.types.tag_set


class DeleteTagsRequest(TypedDict):
    configuration_ids: "aws_sdk_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    """<p>A list of configuration items with tags that you want to delete.</p>"""
    tags: NotRequired["aws_sdk_application_discovery_service.types.tag_set.TagSet"]
    """<p>Tags that you want to delete from one or more configuration items. Specify the tags that you want to delete in a <i>key</i>-<i>value</i> format. For example:</p> <p> <code>{\"key\": \"serverType\", \"value\": \"webServer\"}</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagsRequest) -> dict:
    out: dict = {}
    import aws_sdk_application_discovery_service.types.configuration_id_list

    out["configurationIds"] = (
        aws_sdk_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
            value["configuration_ids"]
        )
    )
    if "tags" in value:
        import aws_sdk_application_discovery_service.types.tag_set

        out["tags"] = (
            aws_sdk_application_discovery_service.types.tag_set.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagsRequest:
    out: DeleteTagsRequest = {}  # type: ignore[typeddict-item]
    if "configurationIds" in data:
        import aws_sdk_application_discovery_service.types.configuration_id_list

        out["configuration_ids"] = (
            aws_sdk_application_discovery_service.types.configuration_id_list.deserialize_aws_json_1_1(
                data["configurationIds"]
            )
        )
    else:
        raise DeserializationError("DeleteTagsRequest.configuration_ids required")
    if "tags" in data:
        import aws_sdk_application_discovery_service.types.tag_set

        out["tags"] = (
            aws_sdk_application_discovery_service.types.tag_set.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    return out
