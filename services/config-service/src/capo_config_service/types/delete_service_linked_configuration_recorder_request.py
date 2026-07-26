"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteServiceLinkedConfigurationRecorderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.service_principal


class DeleteServiceLinkedConfigurationRecorderRequest(TypedDict, closed=True):
    service_principal: "capo_config_service.types.service_principal.ServicePrincipal"
    """<p>The service principal of the Amazon Web Services service for the service-linked configuration recorder that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteServiceLinkedConfigurationRecorderRequest,
) -> dict:
    out: dict = {}
    out["ServicePrincipal"] = value["service_principal"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteServiceLinkedConfigurationRecorderRequest:
    out: DeleteServiceLinkedConfigurationRecorderRequest = {}  # type: ignore[typeddict-item]
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        raise DeserializationError(
            "DeleteServiceLinkedConfigurationRecorderRequest.service_principal required"
        )
    return out
