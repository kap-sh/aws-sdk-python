"""Generated from Smithy shape ``com.amazonaws.bedrock#GetFoundationModelAvailabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.agreement_availability
    import capo_bedrock.types.authorization_status
    import capo_bedrock.types.bedrock_model_id
    import capo_bedrock.types.entitlement_availability
    import capo_bedrock.types.region_availability


class GetFoundationModelAvailabilityResponse(TypedDict, closed=True):
    model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>The model Id of the foundation model.</p>"""
    agreement_availability: (
        "capo_bedrock.types.agreement_availability.AgreementAvailability"
    )
    """<p>Agreement availability. </p>"""
    authorization_status: "capo_bedrock.types.authorization_status.AuthorizationStatus"
    """<p>Authorization status.</p>"""
    entitlement_availability: (
        "capo_bedrock.types.entitlement_availability.EntitlementAvailability"
    )
    """<p>Entitlement availability. </p>"""
    region_availability: "capo_bedrock.types.region_availability.RegionAvailability"
    """<p>Region availability. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFoundationModelAvailabilityResponse) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import capo_bedrock.types.agreement_availability

    out["agreementAvailability"] = (
        capo_bedrock.types.agreement_availability.serialize_json(
            value["agreement_availability"]
        )
    )
    import capo_bedrock.types.authorization_status

    out["authorizationStatus"] = capo_bedrock.types.authorization_status.serialize_json(
        value["authorization_status"]
    )
    import capo_bedrock.types.entitlement_availability

    out["entitlementAvailability"] = (
        capo_bedrock.types.entitlement_availability.serialize_json(
            value["entitlement_availability"]
        )
    )
    import capo_bedrock.types.region_availability

    out["regionAvailability"] = capo_bedrock.types.region_availability.serialize_json(
        value["region_availability"]
    )
    return out


def deserialize_json(data: dict) -> GetFoundationModelAvailabilityResponse:
    out: GetFoundationModelAvailabilityResponse = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "GetFoundationModelAvailabilityResponse.model_id required"
        )
    if data.get("agreementAvailability") is not None:
        import capo_bedrock.types.agreement_availability

        out["agreement_availability"] = (
            capo_bedrock.types.agreement_availability.deserialize_json(
                data["agreementAvailability"]
            )
        )
    else:
        raise DeserializationError(
            "GetFoundationModelAvailabilityResponse.agreement_availability required"
        )
    if data.get("authorizationStatus") is not None:
        import capo_bedrock.types.authorization_status

        out["authorization_status"] = (
            capo_bedrock.types.authorization_status.deserialize_json(
                data["authorizationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "GetFoundationModelAvailabilityResponse.authorization_status required"
        )
    if data.get("entitlementAvailability") is not None:
        import capo_bedrock.types.entitlement_availability

        out["entitlement_availability"] = (
            capo_bedrock.types.entitlement_availability.deserialize_json(
                data["entitlementAvailability"]
            )
        )
    else:
        raise DeserializationError(
            "GetFoundationModelAvailabilityResponse.entitlement_availability required"
        )
    if data.get("regionAvailability") is not None:
        import capo_bedrock.types.region_availability

        out["region_availability"] = (
            capo_bedrock.types.region_availability.deserialize_json(
                data["regionAvailability"]
            )
        )
    else:
        raise DeserializationError(
            "GetFoundationModelAvailabilityResponse.region_availability required"
        )
    return out
