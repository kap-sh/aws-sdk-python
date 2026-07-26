"""Generated from Smithy shape ``com.amazonaws.configservice#PutServiceLinkedConfigurationRecorderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.service_principal
    import capo_config_service.types.tags_list


class PutServiceLinkedConfigurationRecorderRequest(TypedDict, closed=True):
    service_principal: "capo_config_service.types.service_principal.ServicePrincipal"
    """<p>The service principal of the Amazon Web Services service for the service-linked configuration recorder that you want to create.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>The tags for a service-linked configuration recorder. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutServiceLinkedConfigurationRecorderRequest) -> dict:
    out: dict = {}
    out["ServicePrincipal"] = value["service_principal"]
    if "tags" in value:
        import capo_config_service.types.tags_list

        out["Tags"] = capo_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PutServiceLinkedConfigurationRecorderRequest:
    out: PutServiceLinkedConfigurationRecorderRequest = {}  # type: ignore[typeddict-item]
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        raise DeserializationError(
            "PutServiceLinkedConfigurationRecorderRequest.service_principal required"
        )
    if "Tags" in data:
        import capo_config_service.types.tags_list

        out["tags"] = capo_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
