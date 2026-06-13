"""Generated from Smithy shape ``com.amazonaws.bedrock#GetFoundationModelAvailabilityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.agreement_availability
    import aws_sdk_bedrock.types.authorization_status
    import aws_sdk_bedrock.types.bedrock_model_id
    import aws_sdk_bedrock.types.entitlement_availability
    import aws_sdk_bedrock.types.region_availability


class GetFoundationModelAvailabilityResponse(TypedDict):
    model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>The model Id of the foundation model.</p>"""
    agreement_availability: (
        "aws_sdk_bedrock.types.agreement_availability.AgreementAvailability"
    )
    """<p>Agreement availability. </p>"""
    authorization_status: (
        "aws_sdk_bedrock.types.authorization_status.AuthorizationStatus"
    )
    """<p>Authorization status.</p>"""
    entitlement_availability: (
        "aws_sdk_bedrock.types.entitlement_availability.EntitlementAvailability"
    )
    """<p>Entitlement availability. </p>"""
    region_availability: "aws_sdk_bedrock.types.region_availability.RegionAvailability"
    """<p>Region availability. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFoundationModelAvailabilityResponse) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import aws_sdk_bedrock.types.agreement_availability

    out["agreementAvailability"] = (
        aws_sdk_bedrock.types.agreement_availability.serialize_json(
            value["agreement_availability"]
        )
    )
    import aws_sdk_bedrock.types.authorization_status

    out["authorizationStatus"] = (
        aws_sdk_bedrock.types.authorization_status.serialize_json(
            value["authorization_status"]
        )
    )
    import aws_sdk_bedrock.types.entitlement_availability

    out["entitlementAvailability"] = (
        aws_sdk_bedrock.types.entitlement_availability.serialize_json(
            value["entitlement_availability"]
        )
    )
    import aws_sdk_bedrock.types.region_availability

    out["regionAvailability"] = (
        aws_sdk_bedrock.types.region_availability.serialize_json(
            value["region_availability"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetFoundationModelAvailabilityResponse:
    out: GetFoundationModelAvailabilityResponse = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "GetFoundationModelAvailabilityResponse.model_id required"
        )
    if "agreementAvailability" in data:
        import aws_sdk_bedrock.types.agreement_availability

        out["agreement_availability"] = (
            aws_sdk_bedrock.types.agreement_availability.deserialize_json(
                data["agreementAvailability"]
            )
        )
    else:
        raise DeserializationError(
            "GetFoundationModelAvailabilityResponse.agreement_availability required"
        )
    if "authorizationStatus" in data:
        import aws_sdk_bedrock.types.authorization_status

        out["authorization_status"] = (
            aws_sdk_bedrock.types.authorization_status.deserialize_json(
                data["authorizationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "GetFoundationModelAvailabilityResponse.authorization_status required"
        )
    if "entitlementAvailability" in data:
        import aws_sdk_bedrock.types.entitlement_availability

        out["entitlement_availability"] = (
            aws_sdk_bedrock.types.entitlement_availability.deserialize_json(
                data["entitlementAvailability"]
            )
        )
    else:
        raise DeserializationError(
            "GetFoundationModelAvailabilityResponse.entitlement_availability required"
        )
    if "regionAvailability" in data:
        import aws_sdk_bedrock.types.region_availability

        out["region_availability"] = (
            aws_sdk_bedrock.types.region_availability.deserialize_json(
                data["regionAvailability"]
            )
        )
    else:
        raise DeserializationError(
            "GetFoundationModelAvailabilityResponse.region_availability required"
        )
    return out
